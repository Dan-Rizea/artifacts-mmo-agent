import requests
from typing import Optional, List, Dict, Any
from langchain_core.tools import tool

@tool
def ask_game_assistant_game_assistant_ask_post(question: str, pay_with_gems: Optional[bool] = None, token: str = ''):
    """Ask the game assistant a question about game mechanics or public API usage. An active membership is required. Members receive a limited number of free questions per day. When no free question is available, the request can spend 1 gem with pay_with_gems=true.
    
    Args:
        question (str): Your question
        pay_with_gems (bool): Spend 1 gem if no free member question is available.
        token (str): JWT token for authentication.
    """
    url = f"https://api.artifactsmmo.com/game_assistant/ask"
    headers = {"Accept": "application/json"}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    params = {}
    json_data = {"question": question, "pay_with_gems": pay_with_gems}
    json_data = {k: v for k, v in json_data.items() if v is not None}
    response = requests.post(url, headers=headers, params=params, json=json_data)
    try:
        return response.json()
    except:
        return response.text