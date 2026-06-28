import requests
from typing import Optional, List, Dict, Any
from langchain_core.tools import tool

@tool
def action_give_gold_my__name__action_give_gold_post(name: str, quantity: int, character: str, token: str = ''):
    """Give gold to another character in your account on the same map.
    
    Args:
        name (str): Name of your character.
        quantity (int): Gold quantity.
        character (str): Character name. The name of the character who will receive the gold.
        token (str): JWT token for authentication.
    """
    url = f"https://api.artifactsmmo.com/my/{name}/action/give/gold"
    url = url.replace("{name}", str(name))
    headers = {"Accept": "application/json"}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    params = {}
    json_data = {"quantity": quantity, "character": character}
    json_data = {k: v for k, v in json_data.items() if v is not None}
    response = requests.post(url, headers=headers, params=params, json=json_data)
    try:
        return response.json()
    except:
        return response.text