import requests
from typing import Optional, List, Dict, Any
from langchain_core.tools import tool

@tool
def get_tasks_reward_tasks_rewards__code__get(code: str):
    """Retrieve the details of a tasks reward.
    
    Args:
        code (str): The code of the tasks reward.
    """
    url = f"https://api.artifactsmmo.com/tasks/rewards/{code}"
    url = url.replace("{code}", str(code))
    headers = {"Accept": "application/json"}
    params = {}
    json_data = None
    response = requests.get(url, headers=headers, params=params, json=json_data)
    try:
        return response.json()
    except:
        return response.text