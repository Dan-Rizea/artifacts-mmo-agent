import requests
from typing import Optional, List, Dict, Any
from langchain_core.tools import tool
from ._cooldown_decorator import await_cooldown

@tool
@await_cooldown
def action_move_my__name__action_move_post(name: str, x: Optional[int] = None, y: Optional[int] = None, map_id: Optional[int] = None, token: str = ''):
    """Moves a character on the map using either the map's ID or X and Y position. Provide either 'map_id' or both 'x' and 'y' coordinates in the request body.
    
    Args:
        name (str): Name of your character.
        x (int): The x coordinate of the destination.
        y (int): The y coordinate of the destination.
        map_id (int): The map ID of the destination.
        token (str): JWT token for authentication.
    """
    url = f"https://api.artifactsmmo.com/my/{name}/action/move"
    url = url.replace("{name}", str(name))
    headers = {"Accept": "application/json"}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    params = {}
    json_data = {"x": x, "y": y, "map_id": map_id}
    json_data = {k: v for k, v in json_data.items() if v is not None}
    response = requests.post(url, headers=headers, params=params, json=json_data)
    try:
        return response.json()
    except:
        return response.text