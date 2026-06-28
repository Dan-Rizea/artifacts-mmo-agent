import requests
from typing import Optional, List, Dict, Any
from langchain_core.tools import tool
from ._cooldown_decorator import await_cooldown

@tool
@await_cooldown
def action_ge_create_sell_order_my__name__action_grandexchange_create_sell_order_post(name: str, code: str, quantity: int, price: int, token: str = ''):
    """Create a sell order at the Grand Exchange on the character's map.
    
    Args:
        name (str): Name of your character.
        code (str): Item code.
        quantity (int): Item quantity.
        price (int): Item price per unit.
        token (str): JWT token for authentication.
    """
    url = f"https://api.artifactsmmo.com/my/{name}/action/grandexchange/create_sell_order"
    url = url.replace("{name}", str(name))
    headers = {"Accept": "application/json"}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    params = {}
    json_data = {"code": code, "quantity": quantity, "price": price}
    json_data = {k: v for k, v in json_data.items() if v is not None}
    response = requests.post(url, headers=headers, params=params, json=json_data)
    try:
        return response.json()
    except:
        return response.text