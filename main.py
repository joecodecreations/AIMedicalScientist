# main.py

# Import the hello_world function from the module1.py file in the src package
from src.ai import call_ai

def main():
    message = call_ai()
    print(message)

# Entry point of the application
if __name__ == "__main__":
    main()