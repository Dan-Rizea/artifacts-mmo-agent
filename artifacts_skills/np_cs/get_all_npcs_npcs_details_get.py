import requests
from typing import Optional, List, Dict, Any
from langchain_core.tools import tool

@tool
def get_all_npcs_npcs_details_get(name: Optional[str] = None, type: Optional[str] = None, currency: Optional[str] = None, item: Optional[str] = None, page: Optional[int] = None, size: Optional[int] = None):
    """Fetch NPCs details.
    
    Args:
        name (str): NPC name.
        type (str): Type of NPCs.
        currency (str): Currency code to filter NPCs that trade with this currency.
        item (str): Item code to filter NPCs that trade this item.
        page (int): Page number
        size (int): Page size
    """
    url = f"https://api.artifactsmmo.com/npcs/details"
    headers = {"Accept": "application/json"}
    params = {"name": name, "type": type, "currency": currency, "item": item, "page": page, "size": size}
    params = {k: v for k, v in params.items() if v is not None}
    json_data = None
    response = requests.get(url, headers=headers, params=params, json=json_data)
    try:
        return response.json()
    except:
        return response.text