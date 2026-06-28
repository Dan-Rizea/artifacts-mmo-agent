import requests
from typing import Optional, List, Dict, Any
from langchain_core.tools import tool

@tool
def get_accounts_leaderboard_leaderboard_accounts_get(sort: Optional[str] = None, name: Optional[str] = None, page: Optional[int] = None, size: Optional[int] = None):
    """Fetch leaderboard details.
    
    Args:
        sort (str): Sort of account leaderboards.
        name (str): Account name.
        page (int): Page number
        size (int): Page size
    """
    url = f"https://api.artifactsmmo.com/leaderboard/accounts"
    headers = {"Accept": "application/json"}
    params = {"sort": sort, "name": name, "page": page, "size": size}
    params = {k: v for k, v in params.items() if v is not None}
    json_data = None
    response = requests.get(url, headers=headers, params=params, json=json_data)
    try:
        return response.json()
    except:
        return response.text