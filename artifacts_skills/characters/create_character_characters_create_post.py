import requests
from typing import Optional, List, Dict, Any
from langchain_core.tools import tool

@tool
def create_character_characters_create_post(name: str, skin: str, token: str = ''):
    """Create new character on your account. You can create up to 5 characters.
    
    Args:
        name (str): Your desired character name. It's unique and all players can see it.
        skin (str): Your desired skin.
        token (str): JWT token for authentication.
    """
    url = f"https://api.artifactsmmo.com/characters/create"
    headers = {"Accept": "application/json"}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    params = {}
    json_data = {"name": name, "skin": skin}
    json_data = {k: v for k, v in json_data.items() if v is not None}
    response = requests.post(url, headers=headers, params=params, json=json_data)
    try:
        return response.json()
    except:
        return response.text