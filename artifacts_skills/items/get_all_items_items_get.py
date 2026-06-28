import requests
from typing import Optional, List, Dict, Any
from langchain_core.tools import tool

@tool
def get_all_items_items_get(name: Optional[str] = None, min_level: Optional[int] = None, max_level: Optional[int] = None, type: Optional[str] = None, craft_skill: Optional[str] = None, craft_material: Optional[str] = None, page: Optional[int] = None, size: Optional[int] = None):
    """Fetch items details.
    
    Args:
        name (str): Name of the item.
        min_level (int): Minimum level.
        max_level (int): Maximum level.
        type (str): Type of items.
        craft_skill (str): Skill to craft items.
        craft_material (str): Item code of items used as material for crafting.
        page (int): Page number
        size (int): Page size
    """
    url = f"https://api.artifactsmmo.com/items"
    headers = {"Accept": "application/json"}
    params = {"name": name, "min_level": min_level, "max_level": max_level, "type": type, "craft_skill": craft_skill, "craft_material": craft_material, "page": page, "size": size}
    params = {k: v for k, v in params.items() if v is not None}
    json_data = None
    response = requests.get(url, headers=headers, params=params, json=json_data)
    try:
        return response.json()
    except:
        return response.text