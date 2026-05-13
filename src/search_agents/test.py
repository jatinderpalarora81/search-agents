"""Sample script to connect to Claude using LangChain library
"""

import os
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_anthropic import ChatAnthropic

# Load environment variables from .env file
load_dotenv()

# Initialize the Claude model
def initialize_claude_client():
    """
    Initialize Claude client using langchain
    
    The API key is read from the CLAUDE_API_KEY environment variable.
    Make sure to set it in your .env file or system environment.
    """
    api_key = os.getenv("CLAUDE_API_KEY")
    
    if not api_key:
        raise ValueError("CLAUDE_API_KEY environment variable not set")
    
    # Initialize Claude model
    llm = ChatAnthropic(
        api_key=api_key,
        model="claude-sonnet-4-20250514", 
        temperature=0.7,
        max_tokens=500
    )
    
    return llm


def chat_with_claude(user_message: str):
    """
    Send a message to Claude and get a response
    
    Args:
        user_message: The message to send to Claude
        
    Returns:
        The response from Claude
    """
    llm = initialize_claude_client()
    
    # Create messages for the conversation
    messages = [
        SystemMessage(content="You are a helpful assistant."),
        HumanMessage(content=user_message)
    ]
    
    # Get response from Claude
    response = llm.invoke(messages)
    
    return response.content


if __name__ == "__main__":
    # Example usage
    try:
        user_input = "What is the capital of France?"
        print(f"User: {user_input}")
        
        # Get response from Claude
        response = chat_with_claude(user_input)
        print(f"Assistant: {response}")
        
    except ValueError as e:
        print(f"Error: {e}")
        print("Please set your CLAUDE_API_KEY environment variable in .env file")
