from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain.tools import tool
from langgraph.prebuilt import create_react_agent
from dotenv import load_dotenv

load_dotenv()

@tool
def addition(a: float, b: float) -> str:
    """Useful for performing basic addition of 2 numbers."""
    return f"The sum of {a} and {b} is {a + b}"

@tool
def subtraction(a: float, b:float) -> str:
    """Useful for performing basic subtraction of 2 numbers."""
    return f"The difference of {a} and {b} is {a - b}"

@tool
def multiplication(a: float, b: float) -> str:
    """Useful for performing basic multiplication of 2 numbers."""
    return f"The product of {a} and {b} is {a * b}"

@tool
def division(a: float, b: float) -> str:
    """Useful for performing basic division of 2 numbers."""
    return f"The division of {a} and {b} is {a / b}"

@tool
def remainder(a: float, b: float) -> str:
    """Useful for finding out the remainder of 2 numbers."""
    return f"The remainder of {a} and {b} is {a % b}"

def main():
    model = ChatOpenAI(temperature=0, model="gpt-3.5-turbo-0125")

    tools = [addition, subtraction, division, multiplication, remainder]
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