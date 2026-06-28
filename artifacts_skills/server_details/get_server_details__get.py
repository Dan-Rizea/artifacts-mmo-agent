import requests
from typing import Optional, List, Dict, Any
from langchain_core.tools import tool

@tool
def get_server_details__get():
    """Return the status of the game server.
    
    Args:
    """
    url = f"https://api.artifactsmmo.com/"
    headers = {"Accept": "application/json"}
    params = {}
    json_data = None
    response = requests.get(url, headers=headers, params=params, json=json_data)
    try:
        return response.json()
    except:
        return response.text