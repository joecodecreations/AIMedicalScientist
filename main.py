# main.py
from dotenv import load_dotenv
import os
import json
import shutil

# Import the hello_world function from the module1.py file in the src package

from src.utilities.files import read_settings_ini_file
from src.utilities.files import check_and_clear_data
# Causes
from src.causes import causes
from src.genetic_markers import genetic_markers
from src.treatments.symptomatic_treatments import symptomatic_treatments
from src.treatments.curative_treatments import curative_treatments

load_dotenv()



def storeCategoricalData(data):
     # Convert the string to an array if necessary
    if isinstance(data, str):
        data = json.loads(data)

    # for each item in data array, create a folder with the name of the category if it doesnt already exist
    # create a subfolder within it with the name of the subject
    for item in data:
        if not os.path.exists(f'data/{item["category"]}/{item["subject"]}'):
            os.makedirs(f'data/{item["category"]}/{item["subject"]}')

            

def main():

    # Gather System Settings and flags 
    settings = read_settings_ini_file()

    flags = settings["flags"]

    #Set AI Model
    os.environ['OPENAI_MODEL'] = settings["ai"]["MODEL"]

    # Set Research Topic
    os.environ['RESEARCH_TOPIC'] = settings["software"]["RESEARCH_TOPIC"]
    # Set the software type (e.g. "HEALTHCARE", "RESEARCH", etc.)
    os.environ['SOFTWARE_TYPE'] = settings["software"]["TYPE"]


    # Clear the data folder if the setting is set to true
    if(settings["software"]["CLEAR_DATA_ON_STARTUP"]):
        check_and_clear_data()



    # Gather Categories & Data from AI
    # categorical_data = gather_categorical_data()

    # Create a folder structure based on the categories and subjects
    # storeCategoricalData(categorical_data)

    if(flags['top_level_flags']['causes']):
        causes()

    if(flags['top_level_flags']['genetics']):
        genetic_markers()

    if(flags['top_level_flags']['treatments']):
        symptomatic_treatments()

        curative_treatments()


# Entry point of the application
if __name__ == "__main__":
    main()