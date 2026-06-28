import requests
from typing import Optional, List, Dict, Any
from langchain_core.tools import tool

@tool
def action_ge_fill_my__name__action_grandexchange_fill_post(name: str, id: str, quantity: int, token: str = ''):
    """Sell items to an existing buy order at the Grand Exchange on the character's map.  You will receive the gold immediately. The buyer will receive the items in their pending items.
    
    Args:
        name (str): Name of your character.
        id (str): Buy order id.
        quantity (int): Item quantity to sell.
        token (str): JWT token for authentication.
    """
    url = f"https://api.artifactsmmo.com/my/{name}/action/grandexchange/fill"
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