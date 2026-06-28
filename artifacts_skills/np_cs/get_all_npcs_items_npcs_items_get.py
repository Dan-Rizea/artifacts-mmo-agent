import requests
from typing import Optional, List, Dict, Any
from langchain_core.tools import tool

@tool
def get_all_npcs_items_npcs_items_get(code: Optional[str] = None, npc: Optional[str] = None, currency: Optional[str] = None, page: Optional[int] = None, size: Optional[int] = None):
    """Retrieve the list of all NPC items.
    
    Args:
        code (str): Item code.
        npc (str): NPC code.
        currency (str): Currency code.
        page (int): Page number
        size (int): Page size
    """
    url = f"https://api.artifactsmmo.com/npcs/items"
    headers = {"Accept": "application/json"}
    params = {"code": code, "npc": npc, "currency": currency, "page": page, "size": size}
    params = {k: v for k, v in params.items() if v is not None}
    json_data = None
    response = requests.get(url, headers=headers, params=params, json=json_data)
    try:
        return response.json()
    except:
        return response.text