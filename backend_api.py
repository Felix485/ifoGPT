import openai

# open the key.txt file and add its contents to the api_key variable
with open('key.txt', 'r') as file:
    api_key = file.read().replace('\n', '')

openai.api_key = api_key


def generate_response(prompt):
    # Call the OpenAI API to generate a response
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content":"This is the year 2099.I am a cyberpunk AI. Ask me anything."},{'role': 'user', 'content': prompt}],
        max_tokens=1024,
        n=1,
        temperature=0.5,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.6,
    )
    # Get the response text from the API response
    response_text = response['choices'][0]['message']['content']

    return response_text


prompt = "Translate the following English text to French: 'Hello, how are you?'"
print(generate_response(prompt))




