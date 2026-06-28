import requests
from typing import Optional, List, Dict, Any
from langchain_core.tools import tool

@tool
def fight_simulation_simulation_fight_post(characters: List[Dict[str, Any]], monster: str, iterations: int, token: str = ''):
    """Simulate combat with fake characters against a monster multiple times. Member or founder account required.
    
    Args:
        characters (List[Dict[str, Any]]): List of fake characters (1-3).
        monster (str): Monster code to fight against.
        iterations (int): Number of combat iterations to simulate.
        token (str): JWT token for authentication.
    """
    url = f"https://api.artifactsmmo.com/simulation/fight"
    headers = {"Accept": "application/json"}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    params = {}
    json_data = {"characters": characters, "monster": monster, "iterations": iterations}
    json_data = {k: v for k, v in json_data.items() if v is not None}
    response = requests.post(url, headers=headers, params=params, json=json_data)
    try:
        return response.json()
    except:
        return response.text