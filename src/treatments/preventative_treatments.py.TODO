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
load_dotenv()
data_format = 'Start by providing a bulleted list and then go into detail for each bullet point restating the name and then details of each cause.'
key_document_focus="currative treatment"


def curative_rx_treatments():
    scope="the most typical/common"
    topic="perscription"
    outcome="cure" 
    additionals="This list should not include major medical treatments or proceedures like chemo or surgery."
    data = researcher(key_document_focus, scope, topic, outcome, additionals)
    return data

def curative_vitamin_treatments():
    scope="the most typical/common"
    topic="vitamin"
    outcome="cure" 
    additionals=""
    data = researcher(key_document_focus, scope, topic, outcome, additionals)
    return data

def curative_surgery_treatments():
    scope="the most typical/common"
    topic="surgery"
    outcome="cure" 
    additionals= f"Only list surgical currative process. Do not include perscription, chemo etc. Only show surgical."
    data = researcher(key_document_focus, scope, topic, outcome, additionals)
    return data

def curative_treatments():
    
    rx_data = curative_rx_treatments()
    write_file('treatments/currative','perscription_treatments.txt', rx_data)

    vitamin_data = curative_vitamin_treatments()
    write_file('treatments/currative','vitamin_treatments.txt', vitamin_data)

    surgery_data = curative_surgery_treatments()
    write_file('treatments/currative','surgery_treatments.txt', surgery_data)


