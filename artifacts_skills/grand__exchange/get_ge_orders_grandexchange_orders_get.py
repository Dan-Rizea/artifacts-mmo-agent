import requests
from typing import Optional, List, Dict, Any
from langchain_core.tools import tool

@tool
def get_ge_orders_grandexchange_orders_get(code: Optional[str] = None, account: Optional[str] = None, type: Optional[str] = None, item_type: Optional[str] = None, page: Optional[int] = None, size: Optional[int] = None):
    """Fetch all orders (sell and buy orders).  Use the `type` parameter to filter by order type; when using `account`, `type` is required to keep account searches explicit.
    
    Args:
        code (str): The code of the item.
        account (str): The account that sells or buys items.
        type (str): Filter by order type (sell or buy).
        item_type (str): Filter by item type.
        page (int): Page number
        size (int): Page size
    """
    url = f"https://api.artifactsmmo.com/grandexchange/orders"
    headers = {"Accept": "application/json"}
    params = {"code": code, "account": account, "type": type, "item_type": item_type, "page": page, "size": size}
    params = {k: v for k, v in params.items() if v is not None}
    json_data = None
    response = requests.get(url, headers=headers, params=params, json=json_data)
    try:
        return response.json()
    except:
        return response.text