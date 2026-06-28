import requests
from typing import Optional, List, Dict, Any
from langchain_core.tools import tool

@tool
def get_monster_monsters__code__get(code: str):
    """Retrieve the details of a monster.
    
    Args:
        code (str): The code of the monster.
    """
    url = f"https://api.artifactsmmo.com/monsters/{code}"
    url = url.replace("{code}", str(code))
    headers = {"Accept": "application/json"}
    params = {}
    json_data = None
    response = requests.get(url, headers=headers, params=params, json=json_data)
    try:
        return response.json()
    except:
        return response.text