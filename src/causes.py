from dotenv import load_dotenv
import os
from src.utilities.ai import call_ai
from src.utilities.log import log
key_document_focus = "cause"
load_dotenv()
data_format_causes = 'Start by providing a bulleted list and then go into detail for each bullet point restating the name and then details of each cause.'
from src.utilities.files import write_file


def typical_causes():
    log('INFO', f"Starting typical {key_document_focus}s")
    research_topic = os.getenv("RESEARCH_TOPIC")
    system_message = f'What are typical {key_document_focus}s for {research_topic}.{data_format_causes}'
    typical_causes_data = call_ai(system_message, '')
    write_file('causes','typical_causes.txt', typical_causes_data)
    return

def non_typical_causes():
    log('INFO', f"Starting non-typical {key_document_focus}s")
    research_topic = os.getenv("RESEARCH_TOPIC")
    system_message = f'If there are any non-typical or non-mainstream vetted {key_document_focus}s for {research_topic} list them and only them. Do not include commonly known causes. {data_format_causes}'
    non_typical_causes_data = call_ai(system_message, '')
    write_file('causes','non_typical_causes.txt', non_typical_causes_data)
    return