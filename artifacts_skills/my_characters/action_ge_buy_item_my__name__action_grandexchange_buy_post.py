import requests
from typing import Optional, List, Dict, Any
from langchain_core.tools import tool
from ._cooldown_decorator import await_cooldown

@tool
@await_cooldown
def action_ge_buy_item_my__name__action_grandexchange_buy_post(name: str, id: str, quantity: int, token: str = ''):
    """Buy an item at the Grand Exchange on the character's map.
    
    Args:
        name (str): Name of your character.
        id (str): Order id.
        quantity (int): Item quantity.
        token (str): JWT token for authentication.
    """
    url = f"https://api.artifactsmmo.com/my/{name}/action/grandexchange/buy"
    url = url.replace("{name}", str(name))
    headers = {"Accept": "application/json"}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    params = {}
    json_data = {"id": id, "quantity": quantity}
    json_data = {k: v for k, v in json_data.items() if v is not None}
    response = requests.post(url, headers=headers, params=params, json=json_data)
    try:
        return response.json()
    except:
        return response.text