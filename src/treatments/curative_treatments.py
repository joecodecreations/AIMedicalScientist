# CURATIVE TREATMENTS
#   Curative treatments are therapeutic interventions 
#   that target the root cause of a disease or condition 
#   with the aim of eradicating it. These treatments seek 
#   to fully restore health by addressing the underlying pathology, 
#   leading to a complete and permanent resolution of the disease 
#   or condition. Curative treatments stand in contrast to symptomatic 
#   treatments, which only alleviate symptoms without 
#   resolving the primary cause.

from dotenv import load_dotenv
import os
from src.utilities.files import write_file
from src.utilities.researcher import researcher
from src.utilities.log import log
load_dotenv()
data_format = 'Start by providing a bulleted list and then go into detail for each bullet point restating the name and then details of each cause.'
key_document_focus="currative treatment"


def curative_rx_treatments():
    scope="the most typical/common"
    topic="perscription"
    outcome="cure" 
    additionals="This list should not include major medical treatments or proceedures like chemo or surgery."
    log('INFO', f"Getting {scope} {key_document_focus}s using {topic}s")
    rx_data = researcher(key_document_focus, scope, topic, outcome, additionals)
    write_file('treatments/currative','perscriptions.txt', rx_data)
    os.environ['curative_rx_treatments'] = rx_data
    return

def curative_vitamin_treatments():
    scope="the most typical/common"
    topic="vitamin"
    outcome="cure" 
    additionals=""
    log('INFO', f"Getting {scope} {key_document_focus}s using {topic}s")
    vitamin_data = researcher(key_document_focus, scope, topic, outcome, additionals)
    write_file('treatments/currative','vitamin_treatments.txt', vitamin_data)
    os.environ['curative_vitamin_treatments'] = vitamin_data
    
    return

def curative_surgery_treatments():
    scope="the most typical/common"
    topic="surgery"
    outcome="cure" 
    additionals= f"Only list surgical currative process. Do not include perscription, chemo etc. Only show surgical."
    log('INFO', f"Getting {scope} {key_document_focus}s using {topic}s")
    surgery_data = researcher(key_document_focus, scope, topic, outcome, additionals)
    write_file('treatments/currative','surgery_treatments.txt', surgery_data)
    os.environ['curative_surgery_treatments'] = surgery_data
    return


