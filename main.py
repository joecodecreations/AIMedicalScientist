# main.py
from dotenv import load_dotenv
import os
import json
import shutil

# Import the hello_world function from the module1.py file in the src package
from src.ai import call_ai
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
    categorical_data = gather_categorical_data()

    # Create a folder structure based on the categories and subjects
    storeCategoricalData(categorical_data)

    print(categorical_data)




# Entry point of the application
if __name__ == "__main__":
    main()