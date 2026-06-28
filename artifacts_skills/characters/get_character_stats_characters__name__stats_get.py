import requests
from typing import Optional, List, Dict, Any
from langchain_core.tools import tool

@tool
def get_character_stats_characters__name__stats_get(name: str):
    """Retrieve gameplay statistics for a character.  Stats are only visible if the character's account has an active subscription. Statistics are still collected for all accounts regardless of subscription status.
    
    Args:
        name (str): The name of the character.
    """
    url = f"https://api.artifactsmmo.com/characters/{name}/stats"
    url = url.replace("{name}", str(name))
    headers = {"Accept": "application/json"}
    params = {}
    json_data = None
    response = requests.get(url, headers=headers, params=params, json=json_data)
    try:
        return response.json()
    except:
        return response.text