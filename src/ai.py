import openai 


def callAI():
    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Hello world"}])
    print(completion.choices[0].text)
    return "Hello, world!"