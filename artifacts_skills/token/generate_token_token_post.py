import requests
from typing import Optional, List, Dict, Any
from langchain_core.tools import tool

@tool
def generate_token_token_post(token: str = ''):
    """Use your account as HTTPBasic Auth to generate your token to use the API. You can also generate your token directly on the website.
    
    Args:
        token (str): JWT token for authentication.
    """
    url = f"https://api.artifactsmmo.com/token"
    headers = {"Accept": "application/json"}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    params = {}
    json_data = None
    response = requests.post(url, headers=headers, params=params, json=json_data)
    try:
        return response.json()
    except:
        return response.text