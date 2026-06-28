from artifacts_skills import *
import artifacts_skills

# Grouping tools by tags based on the generated modules
import artifacts_skills.my_characters as my_characters
import artifacts_skills.my_account as my_account
import artifacts_skills.server_details as server_details
import artifacts_skills.grand__exchange as grand_exchange
import artifacts_skills.items as items
import artifacts_skills.maps as maps
import artifacts_skills.monsters as monsters
import artifacts_skills.resources as resources
import artifacts_skills.events as events

def get_tools_by_module(module):
    return [getattr(module, name) for name in module.__all__]

def get_character_tools():
    """Returns all tools related to character actions (move, fight, craft, etc.)"""
    return get_tools_by_module(my_characters)

def get_account_tools():
    """Returns all tools related to bank, details, and account management."""
    return get_tools_by_module(my_account)

def get_market_tools():
    """Returns all tools related to the Grand Exchange."""
    return get_tools_by_module(grand_exchange)

def get_game_data_tools():
    """Returns all tools related to fetching game data (items, maps, monsters, resources)."""
    tools = []
    for mod in [items, maps, monsters, resources, events, server_details]:
        tools.extend(get_tools_by_module(mod))
    return tools

def get_all_tools():
    """Returns all tools."""
    tools = []
    for skill_name in artifacts_skills.__all__:
        tools.append(getattr(artifacts_skills, skill_name))
    return tools
