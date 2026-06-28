import requests
from typing import Optional, List, Dict, Any
from langchain_core.tools import tool

@tool
def get_character_characters__name__get(name: str):
    """Retrieve the details of a character.
    
    Args:
        name (str): The name of the character.
    """
    url = f"https://api.artifactsmmo.com/characters/{name}"
    url = url.replace("{name}", str(name))
    headers = {"Accept": "application/json"}
    params = {}
    json_data = None
    response = requests.get(url, headers=headers, params=params, json=json_data)
    try:
        return response.json()
    except:
        return response.text