import requests
from typing import Optional, List, Dict, Any
from langchain_core.tools import tool

@tool
def reset_password_accounts_reset_password_post(token: str, new_password: str):
    """Reset password with a token. Use /forgot_password to get a token by email.
    
    Args:
        token (str): Password reset token.
        new_password (str): Your new password.
    """
    url = f"https://api.artifactsmmo.com/accounts/reset_password"
    headers = {"Accept": "application/json"}
    params = {}
    json_data = {"token": token, "new_password": new_password}
    json_data = {k: v for k, v in json_data.items() if v is not None}
    response = requests.post(url, headers=headers, params=params, json=json_data)
    try:
        return response.json()
    except:
        return response.text