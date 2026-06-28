import requests
from typing import Optional, List, Dict, Any
from langchain_core.tools import tool

@tool
def get_raid_leaderboard_raids__code__leaderboard_get(code: str, page: Optional[int] = None, size: Optional[int] = None):
    """Retrieve the leaderboard for the active or latest raid instance.
    
    Args:
        code (str): The code of the raid.
        page (int): Page number
        size (int): Page size
    """
    url = f"https://api.artifactsmmo.com/raids/{code}/leaderboard"
    url = url.replace("{code}", str(code))
    headers = {"Accept": "application/json"}
    params = {"page": page, "size": size}
    params = {k: v for k, v in params.items() if v is not None}
    json_data = None
    response = requests.get(url, headers=headers, params=params, json=json_data)
    try:
        return response.json()
    except:
        return response.text