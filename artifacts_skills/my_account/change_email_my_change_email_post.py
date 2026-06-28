import requests
from typing import Optional, List, Dict, Any
from langchain_core.tools import tool

@tool
def change_email_my_change_email_post(current_email: str, new_email: str, token: str = ''):
    """Change your account email.
    
    Args:
        current_email (str): Your current email.
        new_email (str): New email.
        token (str): JWT token for authentication.
    """
    url = f"https://api.artifactsmmo.com/my/change_email"
    headers = {"Accept": "application/json"}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    params = {}
    json_data = {"current_email": current_email, "new_email": new_email}
    json_data = {k: v for k, v in json_data.items() if v is not None}
    response = requests.post(url, headers=headers, params=params, json=json_data)
    try:
        return response.json()
    except:
        return response.text