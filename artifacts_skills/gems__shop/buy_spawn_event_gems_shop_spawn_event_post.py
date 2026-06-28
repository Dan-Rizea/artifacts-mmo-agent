import requests
from typing import Optional, List, Dict, Any
from langchain_core.tools import tool

@tool
def buy_spawn_event_gems_shop_spawn_event_post(code: str, token: str = ''):
    """Spawn an event from the gems shop using gems.
    
    Args:
        code (str): Code of the event to spawn
        token (str): JWT token for authentication.
    """
    url = f"https://api.artifactsmmo.com/gems_shop/spawn_event"
    headers = {"Accept": "application/json"}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    params = {}
    json_data = {"code": code}
    json_data = {k: v for k, v in json_data.items() if v is not None}
    response = requests.post(url, headers=headers, params=params, json=json_data)
    try:
        return response.json()
    except:
        return response.text