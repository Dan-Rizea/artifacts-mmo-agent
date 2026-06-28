import requests
from typing import Optional, List, Dict, Any
from langchain_core.tools import tool

@tool
def action_give_items_my__name__action_give_item_post(name: str, items: List[Dict[str, Any]], character: str, token: str = ''):
    """Give items to another character in your account on the same map. The cooldown will be 3 seconds multiplied by the number of different items given.
    
    Args:
        name (str): Name of your character.
        items (List[Dict[str, Any]]): List of items to give
        character (str): Character name. The name of the character who will receive the items.
        token (str): JWT token for authentication.
    """
    url = f"https://api.artifactsmmo.com/my/{name}/action/give/item"
    url = url.replace("{name}", str(name))
    headers = {"Accept": "application/json"}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    params = {}
    json_data = {"items": items, "character": character}
    json_data = {k: v for k, v in json_data.items() if v is not None}
    response = requests.post(url, headers=headers, params=params, json=json_data)
    try:
        return response.json()
    except:
        return response.text