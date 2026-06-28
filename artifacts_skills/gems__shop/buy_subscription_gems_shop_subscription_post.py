import requests
from typing import Optional, List, Dict, Any
from langchain_core.tools import tool

@tool
def buy_subscription_gems_shop_subscription_post(token: str = ''):
    """Buy or extend membership by 30 days using gems. Unavailable while a Stripe subscription is active.
    
    Args:
        token (str): JWT token for authentication.
    """
    url = f"https://api.artifactsmmo.com/gems_shop/subscription"
    headers = {"Accept": "application/json"}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    params = {}
    json_data = None
    response = requests.post(url, headers=headers, params=params, json=json_data)
    try:
        return response.json()
    except:
        return response.text