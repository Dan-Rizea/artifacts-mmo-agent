import requests
from typing import Optional, List, Dict, Any
from langchain_core.tools import tool

@tool
def action_accept_new_task_my__name__action_task_new_post(name: str, token: str = ''):
    """Accepting a new task.
    
    Args:
        name (str): Name of your character.
        token (str): JWT token for authentication.
    """
    url = f"https://api.artifactsmmo.com/my/{name}/action/task/new"
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