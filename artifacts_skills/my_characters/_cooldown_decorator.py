from datetime import datetime, timezone
import time
from functools import wraps

import requests


def get_characters(token: str = ""):
    """List of your characters.
    
    Args:
        token (str): JWT token for authentication.
    """
    url = f"https://api.artifactsmmo.com/my/characters"
    headers = {"Accept": "application/json"}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    params = {}
    json_data = None
    response = requests.get(url, headers=headers, params=params, json=json_data)
    try:
        return response.json()
    except:
        return response.text


def await_cooldown(action):
    @wraps(action)
    def wrap_action(*args, **kwargs):
        name = args[0] if args else kwargs.get("name")
        token = args[-1] if args else kwargs.get("token", "")

        if not name:
            return action(*args, **kwargs)

        data = get_characters(token)
        if not isinstance(data, dict) or "data" not in data:
            return action(*args, **kwargs)

        correct_character = None
        for character in data.get("data", []):
            if character.get("name") == name:
                correct_character = character
                break

        if not correct_character:
            return action(*args, **kwargs)

        cooldown = correct_character.get("cooldown_expiration")
        if cooldown:
            try:
                target_time = datetime.fromisoformat(cooldown.replace("Z", "+00:00"))
                now = datetime.now(timezone.utc)
                delay = (target_time - now).total_seconds()
                if delay > 0:
                    time.sleep(delay)
            except Exception:
                pass

        return action(*args, **kwargs)

    return wrap_action
