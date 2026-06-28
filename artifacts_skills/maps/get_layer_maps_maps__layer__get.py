import requests
from typing import Optional, List, Dict, Any
from langchain_core.tools import tool

@tool
def get_layer_maps_maps__layer__get(layer: str, content_type: Optional[str] = None, content_code: Optional[str] = None, hide_blocked_maps: Optional[bool] = None, hide_event: Optional[bool] = None, transition: Optional[Any] = None, page: Optional[int] = None, size: Optional[int] = None):
    """Fetch maps details.
    
    Args:
        layer (str): The layer of the map (interior, overworld, underground).
        content_type (str): Type of maps.
        content_code (str): Content code on the map.
        hide_blocked_maps (bool): When true, excludes maps with access_type 'blocked' from the results.
        hide_event (bool): When true, does not overlay active events on maps.
        transition (Any): Filter maps by transition. True returns only maps with transitions, False returns only maps without.
        page (int): Page number
        size (int): Page size
    """
    url = f"https://api.artifactsmmo.com/maps/{layer}"
    url = url.replace("{layer}", str(layer))
    headers = {"Accept": "application/json"}
    params = {"content_type": content_type, "content_code": content_code, "hide_blocked_maps": hide_blocked_maps, "hide_event": hide_event, "transition": transition, "page": page, "size": size}
    params = {k: v for k, v in params.items() if v is not None}
    json_data = None
    response = requests.get(url, headers=headers, params=params, json=json_data)
    try:
        return response.json()
    except:
        return response.text