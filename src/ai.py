import openai 


def call_ai():
    from dotenv import load_dotenv
    import os

    load_dotenv()

    openai.api_key = os.getenv("OPENAI_API_KEY")

    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Hello world"}])
    return completion.choices[0].message.content
   