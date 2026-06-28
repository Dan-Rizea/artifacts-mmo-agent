import os
import argparse
from langchain.agents import create_agent
from langchain_google_genai import ChatGoogleGenerativeAI
from toolkits import (
    get_character_tools,
    get_account_tools,
    get_market_tools,
    get_game_data_tools,
    get_all_tools
)

DEFAULT_MODEL = "gemini-3.1-flash-lite"


def create_llm(model: str) -> ChatGoogleGenerativeAI:
    """Create a Gemini chat model, using library defaults for Gemini 3+."""
    if "gemini-3" in model:
        return ChatGoogleGenerativeAI(model=model)
    return ChatGoogleGenerativeAI(model=model, temperature=0)


def main():
    parser = argparse.ArgumentParser(description="Play Artifacts MMO with a LangChain Agent")
    parser.add_argument(
        "--toolkit", 
        choices=["all", "character", "account", "market", "data"], 
        default="all", 
        help="Which group of tools to load to manage context window size."
    )
    parser.add_argument(
        "--model",
        default=None,
        help=(
            f"Gemini model to use (default: {DEFAULT_MODEL}, or GEMINI_MODEL env var). "
            "Examples: gemini-3.1-flash-lite, gemini-3.5-flash"
        ),
    )
    args = parser.parse_args()

    print(f"Loading '{args.toolkit}' toolkit...")
    if args.toolkit == "character":
        tools = get_character_tools()
    elif args.toolkit == "account":
        tools = get_account_tools()
    elif args.toolkit == "market":
        tools = get_market_tools()
    elif args.toolkit == "data":
        tools = get_game_data_tools()
    else:
        tools = get_all_tools()
        print("Warning: Loading all tools may consume a lot of context window tokens.")

    # Read system instructions
    with open("agent_instructions.md", "r") as f:
        system_instructions = f.read()

    if "GOOGLE_API_KEY" not in os.environ and "GEMINI_API_KEY" not in os.environ:
        print("Please set GOOGLE_API_KEY or GEMINI_API_KEY to use this script.")
        return

    model = args.model or os.environ.get("GEMINI_MODEL", DEFAULT_MODEL)
    llm = create_llm(model)

    agent_executor = create_agent(
        llm,
        tools,
        system_prompt=system_instructions,
    )

    print("\n--- Artifacts MMO LangChain Agent ---")
    print(f"Model: {model}")
    print("Agent is ready! Type 'quit' to exit.")
    token = input("Enter your Artifacts MMO JWT token (or press Enter if none): ").strip()
    
    while True:
        try:
            user_input = input("\nYou: ")
            if user_input.lower() in ['quit', 'exit']:
                break
            
            # Pass the auth token dynamically alongside the user request so the agent knows it
            full_input = user_input
            if token:
                full_input = f"[Auth Token: {token}]\n" + full_input
            
            response = agent_executor.invoke({"messages": [("user", full_input)]})
            print("\nAgent:", response["messages"][-1].content)
        except KeyboardInterrupt:
            break
        except Exception as e:
            print(f"\nError: {e}")

if __name__ == "__main__":
    main()
