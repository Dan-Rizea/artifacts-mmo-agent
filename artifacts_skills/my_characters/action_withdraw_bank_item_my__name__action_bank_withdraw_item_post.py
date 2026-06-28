import requests
from typing import Optional, List, Dict, Any
from langchain_core.tools import tool

@tool
def action_withdraw_bank_item_my__name__action_bank_withdraw_item_post(name: str, items: List[Dict[str, Any]], token: str = ''):
    """Take items from your bank and put them in the character's inventory. The cooldown will be 3 seconds multiplied by the number of different items withdrawn.
    
    Args:
        name (str): Name of your character.
        items (List[Dict[str, Any]]): 
        token (str): JWT token for authentication.
    """
    url = f"https://api.artifactsmmo.com/my/{name}/action/bank/withdraw/item"
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