import requests
from typing import Optional, List, Dict, Any
from langchain_core.tools import tool
from ._cooldown_decorator import await_cooldown

@tool
@await_cooldown
def action_withdraw_bank_gold_my__name__action_bank_withdraw_gold_post(name: str, quantity: int, token: str = ''):
    """Withdraw gold from your bank.
    
    Args:
        name (str): Name of your character.
        quantity (int): Quantity of gold.
        token (str): JWT token for authentication.
    """
    url = f"https://api.artifactsmmo.com/my/{name}/action/bank/withdraw/gold"
    url = url.replace("{name}", str(name))
    headers = {"Accept": "application/json"}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    params = {}
    json_data = {"quantity": quantity}
    json_data = {k: v for k, v in json_data.items() if v is not None}
    response = requests.post(url, headers=headers, params=params, json=json_data)
    try:
        return response.json()
    except:
        return response.text