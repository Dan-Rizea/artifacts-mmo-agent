import requests
from typing import Optional, List, Dict, Any
from langchain_core.tools import tool
from ._cooldown_decorator import await_cooldown

@tool
@await_cooldown
def action_gathering_my__name__action_gathering_post(name: str, token: str = ''):
    """Harvest a resource on the character's map.
    
    Args:
        name (str): Name of your character.
        token (str): JWT token for authentication.
    """
    url = f"https://api.artifactsmmo.com/my/{name}/action/gathering"
    url = url.replace("{name}", str(name))
    headers = {"Accept": "application/json"}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    params = {}
    json_data = None
    response = requests.post(url, headers=headers, params=params, json=json_data)
    try:
        return response.json()
    except:
        return response.text