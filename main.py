# main.py
from dotenv import load_dotenv
import os
import json
import shutil

# Import the hello_world function from the module1.py file in the src package

# Causes
from src.causes import typical_causes
from src.causes import non_typical_causes

# Genetic Markers
from src.genetic_markers import known_genetic_markers
from src.genetic_markers import speculative_genetic_markers

from src.ai import gather_categorical_data
from src.utilities import write_file
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

    if os.getenv("CLEAR_DATA_ON_STARTUP") != 'false':
        # Delete the folder and all its contents
        if os.path.exists("./data"):
            shutil.rmtree("./data")

        # Create a new, empty folder with the same name
        os.makedirs("./data")
    
    # Gather Categories & Data from AI
    # categorical_data = gather_categorical_data()

    # Create a folder structure based on the categories and subjects
    # storeCategoricalData(categorical_data)

    # Gather Typical Causes & Data from AI
    typical_causes_data = typical_causes()
    write_file('./data/causes','typical_causes.txt', typical_causes_data)

    # Gather Non Typical Causes & Data from AI
    non_typical_causes_data = non_typical_causes()
    write_file('./data/causes','non_typical_causes.txt', non_typical_causes_data)


    speculative_genetic_markers_data = speculative_genetic_markers()
    write_file('./data/genetic_markers','speculative.txt', speculative_genetic_markers_data)

    known_genetic_markers_data = known_genetic_markers()
    write_file('./data/genetic_markers','known.txt', known_genetic_markers_data)




# Entry point of the application
if __name__ == "__main__":
    main()