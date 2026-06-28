import requests
from typing import Optional, List, Dict, Any
from langchain_core.tools import tool

@tool
def get_all_active_events_events_active_get(page: Optional[int] = None, size: Optional[int] = None):
    """Fetch active events details.
    
    Args:
        page (int): Page number
        size (int): Page size
    """
    url = f"https://api.artifactsmmo.com/events/active"
    headers = {"Accept": "application/json"}
    params = {"page": page, "size": size}
    params = {k: v for k, v in params.items() if v is not None}
    json_data = None
    response = requests.get(url, headers=headers, params=params, json=json_data)
    try:
        return response.json()
    except:
        return response.text