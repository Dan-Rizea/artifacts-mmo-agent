import requests
from typing import Optional, List, Dict, Any
from langchain_core.tools import tool

@tool
def get_map_by_id_maps_id__map_id__get(map_id: int):
    """Retrieve the details of a map by its unique ID.
    
    Args:
        map_id (int): The unique ID of the map.
    """
    url = f"https://api.artifactsmmo.com/maps/id/{map_id}"
    url = url.replace("{map_id}", str(map_id))
    headers = {"Accept": "application/json"}
    params = {}
    json_data = None
    response = requests.get(url, headers=headers, params=params, json=json_data)
    try:
        return response.json()
    except:
        return response.text