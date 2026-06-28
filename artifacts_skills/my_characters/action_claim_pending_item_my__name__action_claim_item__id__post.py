import requests
from typing import Optional, List, Dict, Any
from langchain_core.tools import tool
from ._cooldown_decorator import await_cooldown

@tool
@await_cooldown
def action_claim_pending_item_my__name__action_claim_item__id__post(name: str, id: str, token: str = ''):
    """Claim a pending item with a specific character.
    
    Args:
        name (str): Name of your character.
        id (str): The ID of the pending item to claim.
        token (str): JWT token for authentication.
    """
    url = f"https://api.artifactsmmo.com/my/{name}/action/claim_item/{id}"
    url = url.replace("{name}", str(name))
    url = url.replace("{id}", str(id))
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