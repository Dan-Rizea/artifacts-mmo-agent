import requests
from typing import Optional, List, Dict, Any
from langchain_core.tools import tool

@tool
def get_account_characters_accounts__account__characters_get(account: str):
    """Account character lists.
    
    Args:
        account (str): The name of the account.
    """
    url = f"https://api.artifactsmmo.com/accounts/{account}/characters"
    url = url.replace("{account}", str(account))
    headers = {"Accept": "application/json"}
    params = {}
    json_data = None
    response = requests.get(url, headers=headers, params=params, json=json_data)
    try:
        return response.json()
    except:
        return response.text