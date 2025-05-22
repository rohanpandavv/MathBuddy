# 🧮 LangChain Math Assistant

A simple AI-powered math assistant using [LangChain](https://python.langchain.com/) and [OpenAI](https://openai.com/), capable of handling basic arithmetic operations and natural conversation.

## Features

- **Conversational AI:** Chat with the assistant in plain English.
- **Math Tools:** Perform addition, subtraction, multiplication, division, square roots, exponents, and more.
- **Real-Time Streaming:** See responses as they are generated.
- **OpenAI Integration:** Powered by OpenAI’s API via LangChain for flexible language understanding.
- **Environment Variables:** Secure usage of API keys with `.env` file.

---

## Table of Contents

- [How It Works](#how-it-works)
- [Quick Start](#quick-start)
- [Adding More Math Tools](#adding-more-math-tools)
- [Understanding the Components](#understanding-the-components)
- [Lowering OpenAI Costs](#lowering-openai-costs)
- [FAQ / Further Reading](#faq--further-reading)

---

## How It Works

- The assistant listens to your input.
- It uses [LangChain agents](https://python.langchain.com/docs/modules/agents/) to reason about your question.
- If your input matches a tool (like math operations), it calls the corresponding Python function.
- The result is streamed to your terminal in real time.

---

## Quick Start

1. **Clone the repository:**
    ```bash
    git clone https://github.com/rohanpandavv/MathBuddy.git
    cd MathBuddy
    ```

2. **Install [uv](https://github.com/astral-sh/uv) (if you don’t have it):**
    ```bash
    pip install uv
    ```

3. **Install dependencies with uv:**
    ```bash
    uv pip install -r requirements.txt
    ```

4. **Set up your `.env` file:**
    ```
    OPENAI_API_KEY=sk-xxxxxx
    ```

5. **Activate the virtual environment:**
    ```bash
    source .venv/bin/activate  
    ```
    or
    ```powershell
    venv\Scripts\activate.bat
    ```

6. **Run the assistant:**
    ```bash
    python main.py
    ```

7. **Example Usage:**
    ```
    You: What is 12 times 9?
    Assistant: The product of 12 and 9 is 108

    You: Square root of 16?
    Assistant: The square root of 16 is 4.0

    You: quit
    ```

---

## Adding More Math Tools

You can add any math operation by creating a new function and decorating it with `@tool`.  
**Example:**

```python
import math
@tool
def factorial(a: float) -> str:
    """Useful for finding out the factorial of a number."""
    return f"The factorial of {a} is {math.factorial(a)}"
```

Add your newly created tools to the `tools` list.

```python
tools = [addition, subtraction, division, multiplication, remainder, root, factorial]
```
---
## Understanding the Components
- **ChatOpenAI**:
A wrapper to access OpenAI’s language models. You can set the temperature parameter (randomness) and model (e.g., gpt-3.5-turbo for lower cost).
<br>

- **HumanMessage**:
Used to represent user input as part of a message sequence for the agent.
<br>


- **@tool Decorator**:
Converts a Python function into a “tool” that the agent can use, guided by the function’s docstring.
<br>


- **create_react_agent**:
Instantiates a LangChain ReAct agent which can **REason** and **ACT** (call tools) based on user input.
<br>


- **agent_executor.stream**:
Streams the assistant’s response in real time, providing a conversational experience.
---

## Tips

- Keep prompts concise.
- Don't add unnecessary history to the prompt.
- **NEVER PUSH .ENV FILES ON ANY VERSION CONTROL**
- **MAKE SURE YOU SAFEGUARD YOUR OPENAI SECRET KEY**
