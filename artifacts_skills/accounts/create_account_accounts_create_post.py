import requests
from typing import Optional, List, Dict, Any
from langchain_core.tools import tool

@tool
def create_account_accounts_create_post(username: str, password: str, email: str):
    """Create Account
    
    Args:
        username (str): Your desired username.
        password (str): Your password.
        email (str): Your email.
    """
    url = f"https://api.artifactsmmo.com/accounts/create"
    headers = {"Accept": "application/json"}
    params = {}
    json_data = {"username": username, "password": password, "email": email}
    json_data = {k: v for k, v in json_data.items() if v is not None}
    response = requests.post(url, headers=headers, params=params, json=json_data)
    try:
        return response.json()
    except:
        return response.text