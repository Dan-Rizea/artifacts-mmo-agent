import requests
from typing import Optional, List, Dict, Any
from langchain_core.tools import tool

@tool
def get_ge_orders_my_grandexchange_orders_get(code: Optional[str] = None, type: Optional[str] = None, page: Optional[int] = None, size: Optional[int] = None, token: str = ''):
    """Fetch your orders details (sell and buy orders).
    
    Args:
        code (str): The code of the item.
        type (str): Filter by order type (sell or buy).
        page (int): Page number
        size (int): Page size
        token (str): JWT token for authentication.
    """
    url = f"https://api.artifactsmmo.com/my/grandexchange/orders"
    headers = {"Accept": "application/json"}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    params = {"code": code, "type": type, "page": page, "size": size}
    params = {k: v for k, v in params.items() if v is not None}
    json_data = None
    response = requests.get(url, headers=headers, params=params, json=json_data)
    try:
        return response.json()
    except:
        return response.text