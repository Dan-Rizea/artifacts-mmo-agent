import requests
from typing import Optional, List, Dict, Any
from langchain_core.tools import tool

@tool
def buy_gems_my_buy_gems_post(quantity: int, token: str = ''):
    """Purchase gems. Returns a Stripe checkout URL for payment.
    
    Args:
        quantity (int): Number of gems to purchase.
        token (str): JWT token for authentication.
    """
    url = f"https://api.artifactsmmo.com/my/buy_gems"
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