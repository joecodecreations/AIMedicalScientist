# SYMPTOMPATIC TREATMENTS 
#   Symptomatic treatments are therapeutic interventions 
#   that target and alleviate the symptoms of a disease 
#   or condition rather than addressing its underlying cause. 
#   These treatments provide relief from discomfort or distressing symptoms, 
#   enabling improved quality of life for the patient. 
#   They are commonly used when the primary cause of the symptoms cannot be cured or fully addressed.

from dotenv import load_dotenv
import os
from src.utilities.files import write_file
from src.utilities.researcher import researcher
from src.utilities.log import log

load_dotenv()
data_format = 'Start by providing a bulleted list and then go into detail for each bullet point restating the name and then details of each cause.'
key_document_focus="currative treatment"
research_topic = os.getenv("RESEARCH_TOPIC")


# Symptomatic Perscriptions
def symptomatic_rx_treatments():
    scope="the most typical/common"
    topic="perscription"
    outcome="symptomatic treatment" #keep singular
    additionals="This list should not include major medical treatments or proceedures like chemo or surgery."
    log('INFO', f"Getting {scope} {key_document_focus}s using {topic}s")
    rx_treatments = researcher(key_document_focus, scope, topic, outcome, additionals)
    write_file('treatments/symptomatic','perscription_treatments.txt', rx_treatments)
    return
# Sym
def symptomatic_vitamin_treatments():
    scope="the most typical/common"
    topic="vitamin"
    outcome="symptomatic treatment" #keep singular
    additionals="Only mention the symptom if a vitamin treatment is a potential whether confirmed or speculative. No perscriptions surgery etc."
    log('INFO', f"Getting {scope} {key_document_focus}s using {topic}s")
    vitamin_data = researcher(key_document_focus, scope, topic, outcome, additionals)
    write_file('treatments/symptomatic','vitamin_treatments.txt', vitamin_data)
    return

def symptomatic_surgery_treatments():
    scope="the most typical/common"
    topic="surgery"
    outcome="symptomatic treatment" #keep singular
    additionals= f"List any sugical proceedures that can be done to eleviate or eliminate any symptoms for {research_topic}. Only show mention symptom if there are confirmed surgical proceedures for it. Do not include perscription, chemo etc. Only show surgical."
    log('INFO', f"Getting {scope} {key_document_focus}s using {topic}s")
    surg_treatments = researcher(key_document_focus, scope, topic, outcome, additionals)
    write_file('treatments/symptomatic','surgery_treatments.txt', surg_treatments)
    return
