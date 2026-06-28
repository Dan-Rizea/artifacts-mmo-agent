import requests
from typing import Optional, List, Dict, Any
from langchain_core.tools import tool

@tool
def get_bank_details_my_bank_get(token: str = ''):
    """Fetch bank details.
    
    Args:
        token (str): JWT token for authentication.
    """
    url = f"https://api.artifactsmmo.com/my/bank"
    headers = {"Accept": "application/json"}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    params = {}
    json_data = None
    response = requests.get(url, headers=headers, params=params, json=json_data)
    try:
        return response.json()
    except:
        return response.text