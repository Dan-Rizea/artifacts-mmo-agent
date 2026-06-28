import requests
from typing import Optional, List, Dict, Any
from langchain_core.tools import tool

@tool
def get_all_monsters_monsters_get(name: Optional[str] = None, min_level: Optional[int] = None, max_level: Optional[int] = None, drop: Optional[str] = None, page: Optional[int] = None, size: Optional[int] = None):
    """Fetch monsters details.
    
    Args:
        name (str): Name of the monster.
        min_level (int): Minimum level.
        max_level (int): Maximum level.
        drop (str): Item code of the drop.
        page (int): Page number
        size (int): Page size
    """
    url = f"https://api.artifactsmmo.com/monsters"
    headers = {"Accept": "application/json"}
    params = {"name": name, "min_level": min_level, "max_level": max_level, "drop": drop, "page": page, "size": size}
    params = {k: v for k, v in params.items() if v is not None}
    json_data = None
    response = requests.get(url, headers=headers, params=params, json=json_data)
    try:
        return response.json()
    except:
        return response.text