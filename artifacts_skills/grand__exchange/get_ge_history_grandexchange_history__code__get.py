import requests
from typing import Optional, List, Dict, Any
from langchain_core.tools import tool

@tool
def get_ge_history_grandexchange_history__code__get(code: str, account: Optional[str] = None, page: Optional[int] = None, size: Optional[int] = None):
    """Fetch the transaction history of the item for the last 7 days (buy and sell orders).
    
    Args:
        code (str): The code of the item.
        account (str): Account involved in the transaction (matches either seller or buyer).
        page (int): Page number
        size (int): Page size
    """
    url = f"https://api.artifactsmmo.com/grandexchange/history/{code}"
    url = url.replace("{code}", str(code))
    headers = {"Accept": "application/json"}
    params = {"account": account, "page": page, "size": size}
    params = {k: v for k, v in params.items() if v is not None}
    json_data = None
    response = requests.get(url, headers=headers, params=params, json=json_data)
    try:
        return response.json()
    except:
        return response.text