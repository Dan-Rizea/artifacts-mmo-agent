import requests
from typing import Optional, List, Dict, Any
from langchain_core.tools import tool

@tool
def get_account_achievements_accounts__account__achievements_get(account: str, type: Optional[str] = None, completed: Optional[bool] = None, page: Optional[int] = None, size: Optional[int] = None):
    """Retrieve the achievements of a account.
    
    Args:
        account (str): The name of the account.
        type (str): Type of achievements.
        completed (bool): Filter by completed achievements.
        page (int): Page number
        size (int): Page size
    """
    url = f"https://api.artifactsmmo.com/accounts/{account}/achievements"
    url = url.replace("{account}", str(account))
    headers = {"Accept": "application/json"}
    params = {"type": type, "completed": completed, "page": page, "size": size}
    params = {k: v for k, v in params.items() if v is not None}
    json_data = None
    response = requests.get(url, headers=headers, params=params, json=json_data)
    try:
        return response.json()
    except:
        return response.text