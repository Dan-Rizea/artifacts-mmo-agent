import requests
from typing import Optional, List, Dict, Any
from langchain_core.tools import tool

@tool
def get_task_tasks_list__code__get(code: str):
    """Retrieve the details of a task.
    
    Args:
        code (str): The code of the task.
    """
    url = f"https://api.artifactsmmo.com/tasks/list/{code}"
    url = url.replace("{code}", str(code))
    headers = {"Accept": "application/json"}
    params = {}
    json_data = None
    response = requests.get(url, headers=headers, params=params, json=json_data)
    try:
        return response.json()
    except:
        return response.text