import requests
from typing import Optional, List, Dict, Any
from langchain_core.tools import tool
from ._cooldown_decorator import await_cooldown

@tool
@await_cooldown
def action_deposit_bank_item_my__name__action_bank_deposit_item_post(name: str, items: List[Dict[str, Any]], token: str = ''):
    """Deposit multiple items in a bank on the character's map. The cooldown will be 3 seconds multiplied by the number of different items deposited.
    
    Args:
        name (str): Name of your character.
        items (List[Dict[str, Any]]): List of items to deposit in the bank.
        token (str): JWT token for authentication.
    """
    url = f"https://api.artifactsmmo.com/my/{name}/action/bank/deposit/item"
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