# main.py
from dotenv import load_dotenv
import os

# Import the hello_world function from the module1.py file in the src package
from src.ai import call_ai
load_dotenv()

def gatherCategoricalData():
    research_topic = os.getenv("RESEARCH_TOPIC")
    data_response_description='and return data in an array of JSON with the topic / category in the key of the json "category" and the listen item in the key of the JSON as "subject"'
    general_details = f'List all keywords I should search for to find the most state of the art treatment and potential cures (even if unproven without sufficient evidence yet such as double blind studies) and add the following categories: "General", "Treatment Approaches", "Advanced and Emerging Therapies", "Drug Names and Agents", "Genetic and Molecular Markers", "Stem Cells", "Miscellaneous","Potential Cures & Speculative Therapies"'
    final_instructions = 'and only return the array and no other text outside. The response should start with a [ and end with a ]'
    system_message = f'{general_details} {data_response_description} for the following topic: {research_topic} {final_instructions}'
    categorical_data = call_ai(system_message, '')
    return categorical_data

def main():
    categorical_data = gatherCategoricalData()
    print(categorical_data)




# Entry point of the application
if __name__ == "__main__":
    main()