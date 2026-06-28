import requests
from typing import Optional, List, Dict, Any
from langchain_core.tools import tool

@tool
def buy_subscription_my_subscribe_stripe_post(plan: str, token: str = ''):
    """Subscribe to become a member and unlock the benefits tied to your selected plan. You will receive a secure Stripe checkout URL to complete the payment.
    
    Args:
        plan (str): Recurring Stripe subscription plan to purchase.
        token (str): JWT token for authentication.
    """
    url = f"https://api.artifactsmmo.com/my/subscribe/stripe"
    headers = {"Accept": "application/json"}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    params = {}
    json_data = {"plan": plan}
    json_data = {k: v for k, v in json_data.items() if v is not None}
    response = requests.post(url, headers=headers, params=params, json=json_data)
    try:
        return response.json()
    except:
        return response.text