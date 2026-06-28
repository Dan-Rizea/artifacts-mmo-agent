import requests
from typing import Optional, List, Dict, Any
from langchain_core.tools import tool

@tool
def get_bank_items_my_bank_items_get(item_code: Optional[str] = None, page: Optional[int] = None, size: Optional[int] = None, token: str = ''):
    """Fetch all items in your bank.
    
    Args:
        item_code (str): Item to search in your bank.
        page (int): Page number
        size (int): Page size
        token (str): JWT token for authentication.
    """
    url = f"https://api.artifactsmmo.com/my/bank/items"
    headers = {"Accept": "application/json"}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    params = {"item_code": item_code, "page": page, "size": size}
    params = {k: v for k, v in params.items() if v is not None}
    json_data = None
    response = requests.get(url, headers=headers, params=params, json=json_data)
    try:
        return response.json()
    except:
        return response.text