import requests
from typing import Optional, List, Dict, Any
from langchain_core.tools import tool

@tool
def get_all_achievements_achievements_get(type: Optional[str] = None, page: Optional[int] = None, size: Optional[int] = None):
    """List of all achievements.
    
    Args:
        type (str): Type of achievements.
        page (int): Page number
        size (int): Page size
    """
    url = f"https://api.artifactsmmo.com/achievements"
    headers = {"Accept": "application/json"}
    params = {"type": type, "page": page, "size": size}
    params = {k: v for k, v in params.items() if v is not None}
    json_data = None
    response = requests.get(url, headers=headers, params=params, json=json_data)
    try:
        return response.json()
    except:
        return response.text