from typing import List, Optional
from langchain_core.tools import tool

from artifacts_skills.my_characters.action_fight_my__name__action_fight_post import action_fight_my__name__action_fight_post
from artifacts_skills.my_characters.action_rest_my__name__action_rest_post import action_rest_my__name__action_rest_post

@tool
def action_fight_my__name__action_fight_multiple_post(name: str, monster_count: int, participants: Optional[List[str]] = None, token: str = ''):
    """Start a fight against a monster on the character's map. Add participants for multi-character fights (up to 3 characters, only for boss).
    
    Args:
        name (str): Name of your character.
        monster_count (int): Number of monsters to fight
        participants (List[str]): Optional list of additional character names to include in the fight (max 2 additional characters).
        token (str): JWT token for authentication.
    """

    for _ in range(monster_count):
        action_fight_my__name__action_fight_post.invoke({
            "name": name,
            "participants": participants,
            "token": token,
        })
        action_rest_my__name__action_rest_post.invoke({
            "name": name,
            "token": token,
        })

    return f"Fought {monster_count} monsters!"