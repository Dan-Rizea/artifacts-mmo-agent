import requests
from typing import Optional, List, Dict, Any
from langchain_core.tools import tool

@tool
def get_pending_items_my_pending_items_get(page: Optional[int] = None, size: Optional[int] = None, token: str = ''):
    """Retrieve all unclaimed pending items for your account.  These are items from various sources (achievements, grand exchange, events, etc.) that can be claimed by any character on your account using /my/{name}/action/claim/{id}.
    
    Args:
        page (int): Page number
        size (int): Page size
        token (str): JWT token for authentication.
    """
    url = f"https://api.artifactsmmo.com/my/pending_items"
    headers = {"Accept": "application/json"}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    params = {"page": page, "size": size}
    params = {k: v for k, v in params.items() if v is not None}
    json_data = None
    response = requests.get(url, headers=headers, params=params, json=json_data)
    try:
        return response.json()
    except:
        return response.text