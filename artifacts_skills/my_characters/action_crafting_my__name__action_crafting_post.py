import requests
from typing import Optional, List, Dict, Any
from langchain_core.tools import tool

@tool
def action_crafting_my__name__action_crafting_post(name: str, code: str, quantity: Optional[int] = None, token: str = ''):
    """Craft an item. The character must be on a map with a workshop.
    
    Args:
        name (str): Name of your character.
        code (str): Craft code.
        quantity (int): Quantity of items to craft.
        token (str): JWT token for authentication.
    """
    url = f"https://api.artifactsmmo.com/my/{name}/action/crafting"
    url = url.replace("{name}", str(name))
    headers = {"Accept": "application/json"}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    params = {}
    json_data = {"code": code, "quantity": quantity}
    json_data = {k: v for k, v in json_data.items() if v is not None}
    response = requests.post(url, headers=headers, params=params, json=json_data)
    try:
        return response.json()
    except:
        return response.text