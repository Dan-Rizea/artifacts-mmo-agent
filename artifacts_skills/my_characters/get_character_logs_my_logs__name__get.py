import requests
from typing import Optional, List, Dict, Any
from langchain_core.tools import tool

@tool
def get_character_logs_my_logs__name__get(name: str, page: Optional[int] = None, size: Optional[int] = None, token: str = ''):
    """History of the last actions of your character.
    
    Args:
        name (str): Name of your character.
        page (int): Page number
        size (int): Page size
        token (str): JWT token for authentication.
    """
    url = f"https://api.artifactsmmo.com/my/logs/{name}"
    url = url.replace("{name}", str(name))
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