from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain.tools import tool
from langgraph.prebuilt import create_react_agent
from dotenv import load_dotenv

load_dotenv()

@tool
def addition(a: float, b: float) -> str:
    """Useful for performing basic arithmetic calculations with numbers."""
    return f"The sum of {a} and {b} is {a + b}"

def main():
    model = ChatOpenAI(temperature=0)

    tools = [addition]
    agent_executor = create_react_agent(model, tools)

    print("Welcome, I am your AI assistant.")
    print("You can ask me to perform calculations or chat with me.")

    while True:
        user_input = input("\nYou: ").strip()

        if user_input == "quit":
            break

        print("\nAssistant: ", end="")

        for key in agent_executor.stream(
            {"messages": [HumanMessage(content=user_input)]}
        ):
            if "agent" in key and "messages" in key["agent"]:
                for message in key["agent"]["messages"]:
                    print(message.content, end="")
        print()

if __name__ == "__main__":
    main()