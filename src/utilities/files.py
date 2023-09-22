from dotenv import load_dotenv
import os
import json
import shutil   

def write_file(path, filename, content):

    # get the research topic 
    research_topic = os.getenv("RESEARCH_TOPIC")

    # get the software type
    software_type = os.getenv("SOFTWARE_TYPE")

    # replace spaces with underscores for research topic folder
    research_topic = research_topic.replace(" ", "_")

    # set filepath without file once
    filepath = f"./data/{software_type}/{research_topic}/{path}/"

 
    # create the folder path we need to write the file if not already created
    if not os.path.exists(f'{filepath}'):
        os.makedirs(f'{filepath}')

 
    with open(f"{filepath}{filename}", 'w') as f:
        f.write(content)
    
    return


def check_and_clear_data():
    if os.getenv("CLEAR_DATA_ON_STARTUP") != 'false':
        # Delete the folder and all its contents
        if os.path.exists("./data"):
            shutil.rmtree("./data")

        # Create a new, empty folder with the same name
        os.makedirs("./data")

# Reads the config/settings.ini file that controls the software


def read_settings_ini_file():
    import configparser
    config = configparser.ConfigParser()
    config.read('config/settings.ini')

    settings = {
        'software': {
            'RESEARCH_TOPIC': config.get('SOFTWARE', 'RESEARCH_TOPIC'),
            'CLEAR_DATA_ON_STARTUP': config.getboolean('SOFTWARE', 'CLEAR_DATA_ON_STARTUP'),
            'TYPE': config.get('SOFTWARE', 'TYPE'),
        },
        'ai': {
            'MODEL': config.get('AI', 'MODEL'),
        },
        'system': {
            'log_level': config.get('SYSTEM', 'log_level'),
        },
        'flags': {
            'top_level_flags': {
                'treatments': config.getboolean('TOP_LEVEL_FLAGS', 'treatments'),
                'cures': config.getboolean('TOP_LEVEL_FLAGS', 'cures'),
                'research_articles': config.getboolean('TOP_LEVEL_FLAGS', 'research_articles'),
                'causes': config.getboolean('TOP_LEVEL_FLAGS', 'causes'),
                'genetics': config.getboolean('TOP_LEVEL_FLAGS', 'genetics'),
                'symptoms': config.getboolean('TOP_LEVEL_FLAGS', 'symptoms')
            },
            'category_flags': {
                'rx': config.getboolean('TOP_LEVEL_CATEGORY_FLAGS', 'rx'),
                'vitamins': config.getboolean('TOP_LEVEL_CATEGORY_FLAGS', 'vitamins'),
                'surgery': config.getboolean('TOP_LEVEL_CATEGORY_FLAGS', 'surgery'),
                'genetics': config.getboolean('TOP_LEVEL_CATEGORY_FLAGS', 'genetics'),
                'nutritional': config.getboolean('TOP_LEVEL_CATEGORY_FLAGS', 'nutritional'),
                'alternative': config.getboolean('TOP_LEVEL_CATEGORY_FLAGS', 'alternative'),
                'homeopathic': config.getboolean('TOP_LEVEL_CATEGORY_FLAGS', 'homeopathic')
            },
            'cures_flags': {
                'rx': config.getboolean('CURES', 'rx'),
                'vitamins': config.getboolean('CURES', 'vitamins'),
                'genetics': config.getboolean('CURES', 'genetics'),
                'nutritional': config.getboolean('CURES', 'nutritional'),
                'alternative': config.getboolean('CURES', 'alternative'),
                'homeopathic': config.getboolean('CURES', 'homeopathic')
            },
            'symptompatic_flags': {
                'rx': config.getboolean('SYMPTOMPATIC', 'rx'),
                'vitamins': config.getboolean('SYMPTOMPATIC', 'vitamins'),
                'genetics': config.getboolean('SYMPTOMPATIC', 'genetics'),
                'nutritional': config.getboolean('SYMPTOMPATIC', 'nutritional'),
                'alternative': config.getboolean('SYMPTOMPATIC', 'alternative'),
                'homeopathic': config.getboolean('SYMPTOMPATIC', 'homeopathic')
            },
            'preventative_flags': {
                'rx': config.getboolean('PREVENTITIVE', 'rx'),
                'vitamins': config.getboolean('PREVENTITIVE', 'vitamins'),
                'genetics': config.getboolean('PREVENTITIVE', 'genetics'),
                'nutritional': config.getboolean('PREVENTITIVE', 'nutritional'),
                'alternative': config.getboolean('PREVENTITIVE', 'alternative'),
                'homeopathic': config.getboolean('PREVENTITIVE', 'homeopathic')
            }
        }
    }
    # flags_json = json.dumps(flags, index=4)
    return settings
    # # TOP LEVEL FLAGS
    # flag_main_treatments = config.getboolean('TOP_LEVEL_FLAGS','treatments')
    # flag_main_cures = config.getboolean('TOP_LEVEL_FLAGS','cures')
    # flag_main_research = config.getboolean('TOP_LEVEL_FLAGS','research_articles')
    # flag_main_causes = config.getboolean('TOP_LEVEL_FLAGS','causes')
    # flag_main_genetics = config.getboolean('TOP_LEVEL_FLAGS','genetics')
    # flag_main_symptoms = config.getboolean('TOP_LEVEL_FLAGS','symptoms')

    # # CATEGORIES
    # flag_category_rx = config.getboolean('TOP_LEVEL_CATEGORY_FLAGS','rx')
    # flag_category_vitamins = config.getboolean('TOP_LEVEL_CATEGORY_FLAGS','vitamins')
    # flag_category_surgery = config.getboolean('TOP_LEVEL_CATEGORY_FLAGS','surgery')
    # flag_category_genetics = config.getboolean('TOP_LEVEL_CATEGORY_FLAGS','genetics')
    # flag_category_nutritional = config.getboolean('TOP_LEVEL_CATEGORY_FLAGS','nutritional')
    # flag_category_alternative = config.getboolean('TOP_LEVEL_CATEGORY_FLAGS','alternative')
    # flag_category_homeopathic = config.getboolean('TOP_LEVEL_CATEGORY_FLAGS','homeopathic')

    # # CURES SPECIFICS
    # flag_cures_rx = config.getboolean('CURES','rx')
    # flag_cures_vitamins = config.getboolean('CURES','vitamins')
    # flag_cures_genetics = config.getboolean('CURES','genetics')
    # flag_cures_nutritional = config.getboolean('CURES','nutritional')
    # flag_cures_alternative = config.getboolean('CURES','alternative')
    # flag_cures_homeopathic = config.getboolean('CURES','homeopathic')

    # # SYMPTOMATIC SPECIFICS
    # flag_symptompatic_rx = config.getboolean('SYMPTOMPATIC','rx')
    # flag_symptompatic_vitamins = config.getboolean('SYMPTOMPATIC','vitamins')
    # flag_symptompatic_genetics = config.getboolean('SYMPTOMPATIC','genetics')
    # flag_symptompatic_nutritional = config.getboolean('SYMPTOMPATIC','nutritional')
    # flag_symptompatic_alternative = config.getboolean('SYMPTOMPATIC','alternative')
    # flag_symptompatic_homeopathic = config.getboolean('SYMPTOMPATIC','homeopathic')

    # # PREVENTATIVE SPECIFICS
    # flag_preventative_rx = config.getboolean('PREVENTITIVE','rx')
    # flag_preventative_vitamins = config.getboolean('PREVENTITIVE','vitamins')
    # flag_preventative_genetics = config.getboolean('PREVENTITIVE','genetics')
    # flag_preventative_nutritional = config.getboolean('PREVENTITIVE','nutritional')
    # flag_preventative_alternative = config.getboolean('PREVENTITIVE','alternative')
    # flag_preventative_homeopathic = config.getboolean('PREVENTITIVE','homeopathic')
