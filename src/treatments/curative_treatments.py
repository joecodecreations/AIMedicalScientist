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
from src.utilities.researcher import researcher_specific
from src.utilities.log import log

load_dotenv()
research_topic = os.getenv("RESEARCH_TOPIC")
top_level_topic = 'symptom'
file_path = 'treatments/currative'
find_ending_name = 'cures'
main_ask=f"List cures for {research_topic} and then under each {top_level_topic} list the cure for it available one per array but only list"
data_format = 'Respond with Array of JSON for each. Include the Title, a brief summary and sentences to describe how it is used in this situation. For example: [{ title: "Symptom A", summary: "Symptom A is a blank", Sentences: ["Symptom A is typically treated with...", "Also, research has shown that Vitamin A has increased..."] } ]. Then the array contains as many as necessary to list out all of the information'
key_document_focus="currative treatment"



# Symptomatic Perscriptions
def curative_rx_treatments():
    scope="the most typical/common"
    topic="perscription"
    outcome="symptomatic treatment" #keep singular
    additionals=f"{main_ask }{topic}s that only can cure this {top_level_topic} and only list it if there are a {topic} that can cure and not just treat / relief this. {data_format}"
    log('INFO', f"Getting {scope} {key_document_focus}s using {topic}s")
    rx = researcher_specific(additionals, '')
    write_file(file_path, f'perscription_{find_ending_name}.txt', rx)
    os.environ['curative_rx_treatments'] = rx
    return rx
# Sym
def curative_vitamin_treatments():
    scope="the most typical/common"
    topic="vitamin"
    outcome="symptomatic treatment" #keep singular
    additionals=f"{main_ask }{topic}s that can cure this {top_level_topic} not ease or treat but actually cure and only list it if there are a {topic} that can cur but not just treat / relief this. {data_format}"
   
    # additionals="Only mention the symptom if a vitamin treatment is a potential whether confirmed or speculative. No perscriptions surgery etc."
    log('INFO', f"Getting {scope} {key_document_focus}s using {topic}s")
    vitamins = researcher_specific(additionals, '')
    write_file(file_path,f'vitamin_{find_ending_name}.txt', vitamins)
    os.environ['curative_vitamin_treatments'] = vitamins
    return vitamins

def curative_surgery_treatments():
    scope="the most typical/common"
    topic="surgery"
    outcome="symptomatic treatment" #keep singular
    additionals=f"{main_ask }{topic}s that can ease this {top_level_topic} not cure and only list it if there are a {topic} that can treat / relief but not cure this. {data_format}"
    log('INFO', f"Getting {scope} {key_document_focus}s using {topic}s")
    surgery = researcher_specific(additionals, '')
    write_file(file_path, f'surgery_{find_ending_name}.txt', surgery)
    os.environ['curative_surgery_treatments'] = surgery
    return surgery
