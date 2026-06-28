import requests
from typing import Optional, List, Dict, Any
from langchain_core.tools import tool

@tool
def get_ge_history_my_grandexchange_history_get(id: Optional[str] = None, code: Optional[str] = None, page: Optional[int] = None, size: Optional[int] = None, token: str = ''):
    """Fetch your transaction history of the last 7 days (buy and sell orders).
    
    Args:
        id (str): Order ID to search in your history.
        code (str): Item to search in your history.
        page (int): Page number
        size (int): Page size
        token (str): JWT token for authentication.
    """
    url = f"https://api.artifactsmmo.com/my/grandexchange/history"
    headers = {"Accept": "application/json"}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    params = {"id": id, "code": code, "page": page, "size": size}
    params = {k: v for k, v in params.items() if v is not None}
    json_data = None
    response = requests.get(url, headers=headers, params=params, json=json_data)
    try:
        return response.json()
    except:
        return response.text