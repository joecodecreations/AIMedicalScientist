from dotenv import load_dotenv
import os
from src.ai import call_ai
load_dotenv()
data_format_causes = 'Start by providing a bulleted list and then go into detail for each bullet point restating the name and then details of each cause.'

def typical_causes():
    research_topic = os.getenv("RESEARCH_TOPIC")
    system_message = f'What are typical causes for {research_topic}.{data_format_causes}'
    typical_causes_data = call_ai(system_message, '')
    return typical_causes_data

def non_typical_causes():
    research_topic = os.getenv("RESEARCH_TOPIC")
    system_message = f'If there are any non-typical or non-mainstream vetted causes for {research_topic} list them and only them. Do not include commonly known causes. {data_format_causes}'
    typical_causes_data = call_ai(system_message, '')
    return typical_causes_data