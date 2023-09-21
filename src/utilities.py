from dotenv import load_dotenv
import os

def write_file(path,filename, content):
    if not os.path.exists(f'{path}'):
            os.makedirs(f'{path}')
    with open(f"{path}/{filename}", 'w') as f:
        f.write(content)