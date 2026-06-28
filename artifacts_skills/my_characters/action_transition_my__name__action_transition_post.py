import requests
from typing import Optional, List, Dict, Any
from langchain_core.tools import tool

@tool
def action_transition_my__name__action_transition_post(name: str, token: str = ''):
    """Execute a transition from the current map to another layer. The character must be on a map that has a transition available.
    
    Args:
        name (str): Name of your character.
        token (str): JWT token for authentication.
    """
    url = f"https://api.artifactsmmo.com/my/{name}/action/transition"
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