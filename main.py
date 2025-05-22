from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain.tools import tool
from langgraph.prebuilt import create_react_agent
from dotenv import load_dotenv
import math

load_dotenv()

@tool
def addition(numbers: list[float]) -> str:
    """Useful for performing addition of numbers. There should be at least two numbers in `numbers` list."""
    if len(numbers) < 2:
        return "Please pass at least two numbers to perform addition operation on."
    result = sum(numbers)
    return f"The sum of {numbers} is {result}"

@tool
def subtraction(numbers: list[float]) -> str:
    """Useful for performing subtraction of numbers. There should be at least two numbers in `numbers` list."""
    result = numbers[0] - sum(numbers[1:])
    return f"The difference of {numbers} is {result}"

@tool
def multiplication(numbers: list[float]) -> str:
    """Useful for performing addition of numbers. There should be at least two numbers in `numbers` list."""
    return f"The product of {numbers} is {math.prod(numbers)}"

@tool
def division(a: float, b: float) -> str:
    """Useful for performing basic division of 2 numbers."""
    return f"The division of {a} and {b} is {a / b}"

@tool
def remainder(a: float, b: float) -> str:
    """Useful for finding out the remainder of 2 numbers."""
    return f"The remainder of {a} and {b} is {a % b}"

@tool
def root(a: float) -> str:
    """Useful for finding out the square root of a number."""
    return f"The square root of {a} is {math.sqrt(a)}"

def main():
    model = ChatOpenAI(temperature=0, model="gpt-3.5-turbo-0125")

    tools = [addition, subtraction, division, multiplication, remainder, root]
    agent_executor = create_react_agent(model, tools)

    print("Welcome, I am your AI assistant.")
    print("You can ask me to perform calculations or chat with me.")

    while True:
        user_input = input("\nYou: ").strip()

        if user_input.lower() == "quit":
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