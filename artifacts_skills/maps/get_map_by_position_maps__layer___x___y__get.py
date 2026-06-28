import requests
from typing import Optional, List, Dict, Any
from langchain_core.tools import tool

@tool
def get_map_by_position_maps__layer___x___y__get(layer: str, x: int, y: int):
    """Retrieve the details of a map by layer and coordinates.
    
    Args:
        layer (str): The layer of the map (interior, overworld, underground).
        x (int): The position x of the map.
        y (int): The position y of the map.
    """
    url = f"https://api.artifactsmmo.com/maps/{layer}/{x}/{y}"
    url = url.replace("{layer}", str(layer))
    url = url.replace("{x}", str(x))
    url = url.replace("{y}", str(y))
    headers = {"Accept": "application/json"}
    params = {}
    json_data = None
    response = requests.get(url, headers=headers, params=params, json=json_data)
    try:
        return response.json()
    except:
        return response.text