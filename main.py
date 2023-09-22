# main.py
from dotenv import load_dotenv
import os
import json
import multiprocessing as mp


# File Utilities & Logger
from src.utilities.files import read_settings_ini_file
from src.utilities.files import check_and_clear_data
from src.utilities.log import log
from src.utilities.pdf import create_pdf

# Causes
from src.causes import typical_causes
from src.causes import non_typical_causes

# Genetic Markers
from src.genetic_markers import known_genetic_markers
from src.genetic_markers import speculative_genetic_markers

# Symptom Treatments
from src.treatments.symptomatic_treatments import symptomatic_rx_treatments
from src.treatments.symptomatic_treatments import symptomatic_vitamin_treatments
from src.treatments.symptomatic_treatments import symptomatic_surgery_treatments

# Cures
from src.treatments.curative_treatments import curative_rx_treatments
from src.treatments.curative_treatments import curative_vitamin_treatments
from src.treatments.curative_treatments import curative_surgery_treatments

load_dotenv()


def pool_item_completed(args):
    return

def pool_item_error(error):
    print(error)

            

def main():

    log('INFO', 'Starting the application')

    # Gather System Settings and flags from settings.ini
    settings = read_settings_ini_file()

    # sets system flags from from settings.ini
    flags = settings["flags"]

    #Set AI Model from settings.ini
    os.environ['OPENAI_MODEL'] = settings["ai"]["MODEL"]

    # Set Research Topic from settings.ini
    research_topic = settings["software"]["RESEARCH_TOPIC"]
    os.environ['RESEARCH_TOPIC'] = research_topic
    # Sets software type (e.g. "HEALTHCARE", "RESEARCH", etc.) from settings.ini
    os.environ['SOFTWARE_TYPE'] = settings["software"]["TYPE"]
    # Sets log level from settings.ini
    os.environ['LOG_LEVEL'] = settings["system"]["log_level"]

    

    # Clear the data folder if the setting is set to true
    if(settings["software"]["CLEAR_DATA_ON_STARTUP"]):
        check_and_clear_data()

    pool = mp.Pool(mp.cpu_count())

    if(flags['top_level_flags']['causes']):
        pool.apply_async(non_typical_causes, args=(), callback=pool_item_completed, error_callback=pool_item_error)
        pool.apply_async(typical_causes, args=(), callback=pool_item_completed, error_callback=pool_item_error)

    if(flags['top_level_flags']['genetics']):
        pool.apply_async(known_genetic_markers, args=(), callback=pool_item_completed, error_callback=pool_item_error)
        pool.apply_async(speculative_genetic_markers, args=(), callback=pool_item_completed, error_callback=pool_item_error)

    if(flags['top_level_flags']['treatments']):
        pool.apply_async(symptomatic_rx_treatments, args=(), callback=pool_item_completed, error_callback=pool_item_error)
        pool.apply_async(symptomatic_vitamin_treatments, args=(), callback=pool_item_completed, error_callback=pool_item_error)
        pool.apply_async(symptomatic_surgery_treatments, args=(), callback=pool_item_completed, error_callback=pool_item_error)

    if(flags['top_level_flags']['cures']):
        pool.apply_async(curative_rx_treatments, args=(), callback=pool_item_completed, error_callback=pool_item_error)
        pool.apply_async(curative_vitamin_treatments, args=(), callback=pool_item_completed, error_callback=pool_item_error)
        pool.apply_async(curative_surgery_treatments, args=(), callback=pool_item_completed, error_callback=pool_item_error)

    pool.close()
    pool.join()

    research_topic_file_name = research_topic.replace(" ", "_")
    create_pdf("A.I. Medical Scientist", "Hello world", F'/reports/{research_topic_file_name}.pdf')

# Entry point of the application
if __name__ == "__main__":
    main()
    