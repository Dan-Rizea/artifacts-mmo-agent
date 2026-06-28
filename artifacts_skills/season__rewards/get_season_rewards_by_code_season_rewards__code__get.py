import requests
from typing import Optional, List, Dict, Any
from langchain_core.tools import tool

@tool
def get_season_rewards_by_code_season_rewards__code__get(code: str, page: Optional[int] = None, size: Optional[int] = None):
    """List all season rewards matching a specific code.
    
    Args:
        code (str): The code of the season reward.
        page (int): Page number
        size (int): Page size
    """
    url = f"https://api.artifactsmmo.com/season_rewards/{code}"
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