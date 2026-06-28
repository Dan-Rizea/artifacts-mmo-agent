import requests
from typing import Optional, List, Dict, Any
from langchain_core.tools import tool

@tool
def get_all_raids_raids_get(name: Optional[str] = None, active: Optional[Any] = None, page: Optional[int] = None, size: Optional[int] = None):
    """Fetch the list of all raids.
    
    Args:
        name (str): Name of the raid.
        active (Any): Filter raids by active status.
        page (int): Page number
        size (int): Page size
    """
    url = f"https://api.artifactsmmo.com/raids"
    headers = {"Accept": "application/json"}
    params = {"name": name, "active": active, "page": page, "size": size}
    params = {k: v for k, v in params.items() if v is not None}
    json_data = None
    response = requests.get(url, headers=headers, params=params, json=json_data)
    try:
        return response.json()
    except:
        return response.text