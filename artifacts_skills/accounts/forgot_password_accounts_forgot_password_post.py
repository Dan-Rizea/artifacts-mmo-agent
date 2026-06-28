import requests
from typing import Optional, List, Dict, Any
from langchain_core.tools import tool

@tool
def forgot_password_accounts_forgot_password_post(email: str):
    """Request a password reset.
    
    Args:
        email (str): Your email address.
    """
    url = f"https://api.artifactsmmo.com/accounts/forgot_password"
    headers = {"Accept": "application/json"}
    params = {}
    json_data = {"email": email}
    json_data = {k: v for k, v in json_data.items() if v is not None}
    response = requests.post(url, headers=headers, params=params, json=json_data)
    try:
        return response.json()
    except:
        return response.text