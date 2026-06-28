import requests
from typing import Optional, List, Dict, Any
from langchain_core.tools import tool
from ._cooldown_decorator import await_cooldown

@tool
@await_cooldown
def action_change_skin_my__name__action_change_skin_post(name: str, skin: str, token: str = ''):
    """Change the skin of your character.
    
    Args:
        name (str): Name of your character.
        skin (str): Your desired skin.
        token (str): JWT token for authentication.
    """
    url = f"https://api.artifactsmmo.com/my/{name}/action/change_skin"
    url = url.replace("{name}", str(name))
    headers = {"Accept": "application/json"}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    params = {}
    json_data = {"skin": skin}
    json_data = {k: v for k, v in json_data.items() if v is not None}
    response = requests.post(url, headers=headers, params=params, json=json_data)
    try:
        return response.json()
    except:
        return response.text