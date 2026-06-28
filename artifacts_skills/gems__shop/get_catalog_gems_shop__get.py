import requests
from typing import Optional, List, Dict, Any
from langchain_core.tools import tool

@tool
def get_catalog_gems_shop__get():
    """Return the gems shop catalog.
    
    Args:
    """
    url = f"https://api.artifactsmmo.com/gems_shop/"
    headers = {"Accept": "application/json"}
    params = {}
    json_data = None
    response = requests.get(url, headers=headers, params=params, json=json_data)
    try:
        return response.json()
    except:
        return response.text