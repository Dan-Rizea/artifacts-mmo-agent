import requests
from typing import Optional, List, Dict, Any
from langchain_core.tools import tool

@tool
def cancel_subscription_my_subscribe_cancel_post(token: str = ''):
    """Cancel subscription at the end of the current billing period.
    
    Args:
        token (str): JWT token for authentication.
    """
    url = f"https://api.artifactsmmo.com/my/subscribe/cancel"
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