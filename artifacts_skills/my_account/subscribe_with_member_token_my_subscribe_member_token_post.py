import requests
from typing import Optional, List, Dict, Any
from langchain_core.tools import tool

@tool
def subscribe_with_member_token_my_subscribe_member_token_post(token: str = ''):
    """Redeem a member token to start or extend membership by 30 days. Member tokens are manually granted as rewards for events. Member tokens cannot be redeemed while a Stripe subscription is active.
    
    Args:
        token (str): JWT token for authentication.
    """
    url = f"https://api.artifactsmmo.com/my/subscribe/member_token"
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