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

def gather_categorical_data():
    research_topic = os.getenv("RESEARCH_TOPIC")
    categories = os.getenv('DATA_CATEGORIES')
    data_response_description='and return data in an array of JSON with the topic / category in the key of the json "category" and the listen item in the key of the JSON as "subject"'
    general_details = f'List all keywords I should search for to find the most state of the art treatment and potential cures (even if unproven without sufficient evidence yet such as double blind studies) and add the following categories: {categories}'
    final_instructions = 'and only return the array and no other text outside. The response should start with a [ and end with a ]'
    system_message = f'{general_details} {data_response_description} for the following topic: {research_topic} {final_instructions}'
    categorical_data = call_ai(system_message, '')
    return categorical_data


def typical_causes():
    research_topic = os.getenv("RESEARCH_TOPIC")
    system_message = f'What are typical causes for {research_topic}. Start by providing a bulleted list and then go into detail for each bullet point restating the name and then details of each cause.'
    typical_causes_data = call_ai(system_message, '')
    return typical_causes_data