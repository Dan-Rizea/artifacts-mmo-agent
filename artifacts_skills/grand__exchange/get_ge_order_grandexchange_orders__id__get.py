import requests
from typing import Optional, List, Dict, Any
from langchain_core.tools import tool

@tool
def get_ge_order_grandexchange_orders__id__get(id: str):
    """Retrieve a specific order by ID.
    
    Args:
        id (str): The id of the order.
    """
    url = f"https://api.artifactsmmo.com/grandexchange/orders/{id}"
    url = url.replace("{id}", str(id))
    headers = {"Accept": "application/json"}
    params = {}
    json_data = None
    response = requests.get(url, headers=headers, params=params, json=json_data)
    try:
        return response.json()
    except:
        return response.text