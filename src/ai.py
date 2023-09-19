from dotenv import load_dotenv
import os
import openai  # Don't forget to import the openai module

def call_ai(system_message=None, user_content=None):
    # Load environment variables from .env file
    load_dotenv()

    # Retrieve OpenAI API key from environment variables
    api_key = os.getenv("OPENAI_API_KEY")
    OPENAI_MODEL = os.getenv("OPENAI_MODEL")
    openai.api_key = api_key

    # Initialize messages list
    messages = []
    
    # Optionally include a system message
    if system_message is not None:
        messages.append({"role": "system", "content": system_message})
        
    # Include a user message
    if user_content is not None:
        messages.append({"role": "user", "content": user_content})
        
    # If messages list is empty, return an error or a default message
    if not messages:
        return "No messages provided for the API call."
        
    # Make the API call to OpenAI
    completion = openai.ChatCompletion.create(
        model=OPENAI_MODEL,
        messages=messages,
        temperature=1,
        max_tokens=11384,
        top_p=0.06,
        frequency_penalty=0,
        presence_penalty=0
    )
    
    # Return the content of the AI's response
    return completion['choices'][0]['message']['content']