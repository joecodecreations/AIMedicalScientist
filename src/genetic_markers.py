from dotenv import load_dotenv
import os
from src.ai import call_ai
load_dotenv()
data_format = 'Start by providing a bulleted list and then go into detail for each bullet point restating the name and then details of each cause.'

def known_genetic_markers():
    research_topic = os.getenv("RESEARCH_TOPIC")
    system_message = f'What are the known genetic markers for {research_topic}.{data_format}'
    known_genetic_markers_data = call_ai(system_message, '')
    return known_genetic_markers_data

def speculative_genetic_markers():
    research_topic = os.getenv("RESEARCH_TOPIC")
    system_message = f'What are non-confirmed but speculative and yet to be confirmed genetic markers for {research_topic}.{data_format}'
    speculative_genetic_markers_data = call_ai(system_message, '')
    return speculative_genetic_markers_data