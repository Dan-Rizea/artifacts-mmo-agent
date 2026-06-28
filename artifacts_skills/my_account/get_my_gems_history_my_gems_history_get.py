import requests
from typing import Optional, List, Dict, Any
from langchain_core.tools import tool

@tool
def get_my_gems_history_my_gems_history_get(token: str = ''):
    """List all gem credits and debits.
    
    Args:
        token (str): JWT token for authentication.
    """
    url = f"https://api.artifactsmmo.com/my/gems_history"
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