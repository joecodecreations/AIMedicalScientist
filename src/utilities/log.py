import os
import logging
from dotenv import load_dotenv

load_dotenv()

LOG_LEVEL_MAPPING = {
    'VERBOSE': logging.DEBUG,
    'DEBUG': logging.DEBUG,
    'INFO': logging.INFO,
    'WARNING': logging.WARNING,
    'ERROR': logging.ERROR,
    'CRITICAL': logging.CRITICAL,
    'NONE': 100  # custom level to disable all logging
}

LOG_LEVEL = os.getenv("LOG_LEVEL", 'INFO')  # default to INFO if no LOG_LEVEL is provided
logging_level = LOG_LEVEL_MAPPING.get(LOG_LEVEL, logging.INFO)

logging.basicConfig(level=logging_level)
logging.info(f'Logging Level: {LOG_LEVEL}')

def log(level, message):
    if level not in LOG_LEVEL_MAPPING:
        raise ValueError(f"Invalid log level: {level}")

    logger = logging.getLogger()
    if logger.isEnabledFor(LOG_LEVEL_MAPPING[level]):
        getattr(logger, level.lower())(message)

