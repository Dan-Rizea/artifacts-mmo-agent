import time

import requests
from typing import Optional, List, Dict, Any
from langchain_core.tools import tool
from ._cooldown_decorator import await_cooldown

@tool
@await_cooldown
def action_gathering_my__name__action_gathering_multiple_post(name: str, quantity: int, token: str = ''):
    """Harvest a resource on the character's map multiple times.
    
    Args:
        name (str): Name of your character.
        quantity (int): Number of items to gather
        token (str): JWT token for authentication.
    """
    url = f"https://api.artifactsmmo.com/my/{name}/action/gathering"
    url = url.replace("{name}", str(name))
    headers = {"Accept": "application/json"}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    params = {}
    json_data = None

    for _ in range(quantity):
        response = requests.post(url, headers=headers, params=params, json=json_data)
        try:
            data = response.json()
            time.sleep(data["data"]["cooldown"]["total_seconds"]) 
        except:
            return response.text
    
    return f"Successfully gathered {quantity} resources!"
