import requests
from typing import Optional, List, Dict, Any
from langchain_core.tools import tool
from ._cooldown_decorator import await_cooldown

@tool
@await_cooldown
def action_fight_my__name__action_fight_post(name: str, participants: Optional[List[str]] = None, token: str = ''):
    """Start a fight against a monster on the character's map. Add participants for multi-character fights (up to 3 characters, only for boss).
    
    Args:
        name (str): Name of your character.
        participants (List[str]): Optional list of additional character names to include in the fight (max 2 additional characters).
        token (str): JWT token for authentication.
    """
    url = f"https://api.artifactsmmo.com/my/{name}/action/fight"
    url = url.replace("{name}", str(name))
    headers = {"Accept": "application/json"}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    params = {}
    json_data = {"participants": participants}
    json_data = {k: v for k, v in json_data.items() if v is not None}
    response = requests.post(url, headers=headers, params=params, json=json_data)
    try:
        return response.json()
    except:
        return response.text