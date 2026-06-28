import requests
from typing import Optional, List, Dict, Any
from langchain_core.tools import tool
from ._cooldown_decorator import await_cooldown

@tool
@await_cooldown
def action_recycling_my__name__action_recycling_post(name: str, code: str, quantity: Optional[int] = None, enhanced: Optional[bool] = None, token: str = ''):
    """Recycling an item. The character must be on a map with a workshop (only for equipments and weapons).
    
    Args:
        name (str): Name of your character.
        code (str): Item code.
        quantity (int): Quantity of items to recycle.
        enhanced (bool): Whether to use enhanced recycling.
        token (str): JWT token for authentication.
    """
    url = f"https://api.artifactsmmo.com/my/{name}/action/recycling"
    url = url.replace("{name}", str(name))
    headers = {"Accept": "application/json"}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    params = {}
    json_data = {"code": code, "quantity": quantity, "enhanced": enhanced}
    json_data = {k: v for k, v in json_data.items() if v is not None}
    response = requests.post(url, headers=headers, params=params, json=json_data)
    try:
        return response.json()
    except:
        return response.text