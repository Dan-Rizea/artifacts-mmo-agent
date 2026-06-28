import requests
from typing import Optional, List, Dict, Any
from langchain_core.tools import tool

@tool
def delete_character_characters_delete_post(name: str, token: str = ''):
    """Delete character on your account.
    
    Args:
        name (str): Character name.
        token (str): JWT token for authentication.
    """
    url = f"https://api.artifactsmmo.com/characters/delete"
    headers = {"Accept": "application/json"}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    params = {}
    json_data = {"name": name}
    json_data = {k: v for k, v in json_data.items() if v is not None}
    response = requests.post(url, headers=headers, params=params, json=json_data)
    try:
        return response.json()
    except:
        return response.text