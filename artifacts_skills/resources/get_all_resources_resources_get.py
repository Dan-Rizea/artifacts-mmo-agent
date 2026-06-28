import requests
from typing import Optional, List, Dict, Any
from langchain_core.tools import tool

@tool
def get_all_resources_resources_get(min_level: Optional[int] = None, max_level: Optional[int] = None, skill: Optional[str] = None, drop: Optional[str] = None, page: Optional[int] = None, size: Optional[int] = None):
    """Fetch resources details.
    
    Args:
        min_level (int): Minimum level.
        max_level (int): Maximum level.
        skill (str): Skill of resources.
        drop (str): Item code of the drop.
        page (int): Page number
        size (int): Page size
    """
    url = f"https://api.artifactsmmo.com/resources"
    headers = {"Accept": "application/json"}
    params = {"min_level": min_level, "max_level": max_level, "skill": skill, "drop": drop, "page": page, "size": size}
    params = {k: v for k, v in params.items() if v is not None}
    json_data = None
    response = requests.get(url, headers=headers, params=params, json=json_data)
    try:
        return response.json()
    except:
        return response.text