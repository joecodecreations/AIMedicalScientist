from dotenv import load_dotenv
import os

def write_file(path, content):
    with open(path, 'w') as f:
        f.write(content)