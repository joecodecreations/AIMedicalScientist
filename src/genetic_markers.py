from dotenv import load_dotenv
import os
from src.utilities.ai import call_ai
from src.utilities.files import write_file
from src.utilities.log import log
load_dotenv()
data_format = 'Start by providing a bulleted list and then go into detail for each bullet point restating the name and then details of each cause.'
key_document_focus = 'genetic marker'
def known_genetic_markers():
    research_topic = os.getenv("RESEARCH_TOPIC")
    system_message = f'What are the known genetic markers for {research_topic}.{data_format}'
    known_genetic_markers_data = call_ai(system_message, '')
    write_file('genetic_markers','known.txt', known_genetic_markers_data)
    return known_genetic_markers_data

def speculative_genetic_markers():
    research_topic = os.getenv("RESEARCH_TOPIC")
    system_message = f'What are non-confirmed but speculative and yet to be confirmed genetic markers for {research_topic}.{data_format}'
    speculative_genetic_markers_data = call_ai(system_message, '')
    write_file('genetic_markers','speculative.txt', speculative_genetic_markers_data)
    return

def genetic_markers(tasks):
    log('INFO', f"Starting {key_document_focus}s")
    tasks.append(speculative_genetic_markers)
    tasks.append(known_genetic_markers)

    return tasks