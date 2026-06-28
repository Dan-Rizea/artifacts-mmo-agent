import os
import json
import urllib.request
import re

def to_snake_case(name):
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower().replace(' ', '_').replace('-', '_')

def resolve_ref(ref, spec):
    parts = ref.split('/')
    obj = spec
    for part in parts[1:]:
        obj = obj[part]
    return obj

def get_type_hint(prop, spec):
    if "$ref" in prop:
        prop = resolve_ref(prop["$ref"], spec)
    t = prop.get("type", "Any")
    if t == "string": return "str"
    if t == "integer": return "int"
    if t == "boolean": return "bool"
    if t == "number": return "float"
    if t == "array":
        items = prop.get("items", {})
        item_type = get_type_hint(items, spec)
        return f"List[{item_type}]"
    if t == "object": return "Dict[str, Any]"
    return "Any"

def generate_tool_code(path, method, operation, spec):
    tags = operation.get("tags", ["default"])
    tag = to_snake_case(tags[0])
    summary = operation.get("summary", "No summary")
    description = operation.get("description", summary).replace('"', "'").replace('\n', ' ')
    operation_id = operation.get("operationId", to_snake_case(summary))
    
    # We need to construct parameters
    params = []
    func_args = []
    docstring_args = []
    
    # Path/Query parameters
    if "parameters" in operation:
        for p in operation["parameters"]:
            name = p["name"]
            py_name = to_snake_case(name)
            req = p.get("required", False)
            schema = p.get("schema", {})
            t = get_type_hint(schema, spec)
            if not req:
                func_args.append(f"{py_name}: Optional[{t}] = None")
            else:
                func_args.append(f"{py_name}: {t}")
            docstring_args.append(f"{py_name} ({t}): {p.get('description', '')}")

    # Body parameters
    body_schema = None
    if "requestBody" in operation:
        content = operation["requestBody"].get("content", {})
        if "application/json" in content:
            body_schema = content["application/json"].get("schema", {})
            if "$ref" in body_schema:
                body_schema = resolve_ref(body_schema["$ref"], spec)
            
            if body_schema.get("type") == "object":
                props = body_schema.get("properties", {})
                required_props = body_schema.get("required", [])
                for prop_name, prop_details in props.items():
                    py_name = to_snake_case(prop_name)
                    t = get_type_hint(prop_details, spec)
                    is_req = prop_name in required_props
                    if is_req:
                        func_args.append(f"{py_name}: {t}")
                    else:
                        func_args.append(f"{py_name}: Optional[{t}] = None")
                    docstring_args.append(f"{py_name} ({t}): {prop_details.get('description', '')}")
            elif body_schema.get("type") == "array":
                # It's an array body
                items_type = get_type_hint(body_schema.get("items", {}), spec)
                func_args.append(f"items: List[{items_type}]")
                docstring_args.append(f"items (List[{items_type}]): {body_schema.get('description', '')}")
            else:
                # simple type
                func_args.append(f"data: Dict[str, Any]")
                docstring_args.append(f"data (Dict[str, Any]): request body")
    
    # Needs auth?
    security = operation.get("security", [])
    needs_auth = len(security) > 0
    if needs_auth:
        func_args.append("token: str = ''")
        docstring_args.append("token (str): JWT token for authentication.")
        
    args_str = ", ".join(func_args)
    
    # building python code
    lines = []
    lines.append("import requests")
    lines.append("from typing import Optional, List, Dict, Any")
    lines.append("from langchain_core.tools import tool")
    lines.append("")
    lines.append(f"@tool")
    lines.append(f"def {operation_id}({args_str}):")
    lines.append(f'    """{description}')
    lines.append(f"    ")
    lines.append(f"    Args:")
    for d in docstring_args:
        lines.append(f"        {d}")
    lines.append(f'    """')
    # Use f-string to properly format paths like /my/{name}/action/move
    path_formatted = path.replace("{", "{").replace("}", "}")
    lines.append(f'    url = f"https://api.artifactsmmo.com{path}"')
    
    # Path params replacement
    if "parameters" in operation:
        for p in operation["parameters"]:
            if p["in"] == "path":
                py_name = to_snake_case(p["name"])
                lines.append(f'    url = url.replace("{{{p["name"]}}}", str({py_name}))')
                
    lines.append(f'    headers = {{"Accept": "application/json"}}')
    if needs_auth:
        lines.append(f'    if token:')
        lines.append(f'        headers["Authorization"] = f"Bearer {{token}}"')
        
    # Query params
    query_params = []
    if "parameters" in operation:
        for p in operation["parameters"]:
            if p["in"] == "query":
                py_name = to_snake_case(p["name"])
                query_params.append(f'"{p["name"]}": {py_name}')
    
    if query_params:
        lines.append(f'    params = {{{", ".join(query_params)}}}')
        lines.append(f'    params = {{k: v for k, v in params.items() if v is not None}}')
    else:
        lines.append(f'    params = {{}}')
        
    # Request body dict
    if body_schema:
        if body_schema.get("type") == "object":
            props = body_schema.get("properties", {})
            body_dict_items = []
            for prop_name in props.keys():
                py_name = to_snake_case(prop_name)
                body_dict_items.append(f'"{prop_name}": {py_name}')
            lines.append(f'    json_data = {{{", ".join(body_dict_items)}}}')
            lines.append(f'    json_data = {{k: v for k, v in json_data.items() if v is not None}}')
        elif body_schema.get("type") == "array":
            lines.append(f'    json_data = items')
        else:
            lines.append(f'    json_data = data')
    else:
        lines.append(f'    json_data = None')
        
    lines.append(f'    response = requests.{method}(url, headers=headers, params=params, json=json_data)')
    lines.append(f'    try:')
    lines.append(f'        return response.json()')
    lines.append(f'    except:')
    lines.append(f'        return response.text')
    
    return tag, operation_id, "\n".join(lines)


def main():
    print("Fetching OpenAPI Spec...")
    req = urllib.request.Request('https://api.artifactsmmo.com/openapi.json', headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as response:
        spec = json.loads(response.read().decode())
    
    base_dir = "artifacts_skills"
    os.makedirs(base_dir, exist_ok=True)
    
    init_files = {}
    
    for path, methods in spec.get("paths", {}).items():
        for method, operation in methods.items():
            if method not in ["get", "post", "put", "delete", "patch"]:
                continue
                
            tag, op_id, code = generate_tool_code(path, method, operation, spec)
            
            tag_dir = os.path.join(base_dir, tag)
            os.makedirs(tag_dir, exist_ok=True)
            
            # fix op_id replacing dashes or other chars if they exist
            op_id = op_id.replace('-', '_')
            
            file_path = os.path.join(tag_dir, f"{op_id}.py")
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(code)
                
            if tag not in init_files:
                init_files[tag] = []
            init_files[tag].append(op_id)
            
    # write __init__.py files
    all_tools = []
    for tag, ops in init_files.items():
        tag_init = os.path.join(base_dir, tag, "__init__.py")
        with open(tag_init, "w", encoding="utf-8") as f:
            for op in ops:
                f.write(f"from .{op} import {op}\n")
            f.write(f"\n__all__ = {json.dumps(ops)}\n")
            
        all_tools.append((tag, ops))
        
    main_init = os.path.join(base_dir, "__init__.py")
    with open(main_init, "w", encoding="utf-8") as f:
        f.write('"""Artifacts MMO LangChain Skills"""\n\n')
        all_ops = []
        for tag, ops in all_tools:
            for op in ops:
                f.write(f"from .{tag}.{op} import {op}\n")
                all_ops.append(op)
        f.write(f"\n__all__ = {json.dumps(all_ops)}\n")
    print(f"Generated skills in {base_dir} directory.")

if __name__ == '__main__':
    main()
