from dotenv import load_dotenv
import os
from src.utilities.ai import call_ai
from src.utilities.files import write_file
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

def genetic_markers():
    speculative_genetic_markers_data = speculative_genetic_markers()
    write_file('genetic_markers','speculative.txt', speculative_genetic_markers_data)

    known_genetic_markers_data = known_genetic_markers()
    write_file('genetic_markers','known.txt', known_genetic_markers_data)