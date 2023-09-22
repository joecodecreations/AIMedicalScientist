# Currative Treatments are treatments that could end up potentially curring the research_topic

from dotenv import load_dotenv
import os
from src.utilities.ai import call_ai
load_dotenv()



# Scope - the most typical/common
# Topic - perscription
# Outcome - cure
# Negatives - Sentence of what to NOT include 
# Data Format - Describes the format output of the data

def researcher(key_document_focus, scope, topic, outcome, additionals, data_format_incoming=None):
    data_format = 'Start by providing a bulleted list and then go into detail for each bullet point restating the name and then details of each cause.'
    research_topic = os.getenv("RESEARCH_TOPIC")
    
    if data_format_incoming != None:
        data_format = data_format_incoming

    system_message = f'For each {key_document_focus} available for {research_topic}, list each {key_document_focus} and provide {scope} {topic}s used to {outcome} {research_topic} if any. {additionals} {data_format}'
    data = call_ai(system_message, '')
    return data