import requests
from typing import Optional, List, Dict, Any
from langchain_core.tools import tool

@tool
def change_password_my_change_password_post(current_password: str, new_password: str, token: str = ''):
    """Change your account password. Changing the password reset the account token.
    
    Args:
        current_password (str): Your password.
        new_password (str): New password.
        token (str): JWT token for authentication.
    """
    url = f"https://api.artifactsmmo.com/my/change_password"
    headers = {"Accept": "application/json"}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    params = {}
    json_data = {"current_password": current_password, "new_password": new_password}
    json_data = {k: v for k, v in json_data.items() if v is not None}
    response = requests.post(url, headers=headers, params=params, json=json_data)
    try:
        return response.json()
    except:
        return response.text