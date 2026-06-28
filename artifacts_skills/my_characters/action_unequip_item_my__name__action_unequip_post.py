import requests
from typing import Optional, List, Dict, Any
from langchain_core.tools import tool

@tool
def action_unequip_item_my__name__action_unequip_post(name: str, items: List[Dict[str, Any]], token: str = ''):
    """Unequip multiple items on your character. The cooldown will be 3 seconds multiplied by the number of different items unequipped.
    
    Args:
        name (str): Name of your character.
        items (List[Dict[str, Any]]): List of items to unequip.
        token (str): JWT token for authentication.
    """
    url = f"https://api.artifactsmmo.com/my/{name}/action/unequip"
    url = url.replace("{name}", str(name))
    headers = {"Accept": "application/json"}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    params = {}
    json_data = items
    response = requests.post(url, headers=headers, params=params, json=json_data)
    try:
        return response.json()
    except:
        return response.text