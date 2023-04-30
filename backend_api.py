import openai

# Read the API key from the 'key.txt' file and set it as the OpenAI API key
with open('key.txt', 'r') as file:
    api_key = file.read().replace('\n', '')

openai.api_key = api_key


def generate_response(prompt):
    # Call the OpenAI API to generate a response
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "I am a twitter post writer for the ifo Institute. They post short, professional posts with hashtags and links in German "},
            {'role': 'user', 'content': prompt}
        ],
        max_tokens=280,
        stop=None,
        n=1,
        temperature=0.5,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.6,
    )
    # Get the response text from the API response
    response_text = response['choices'][0]['message']['content']

    return response_text


def twitter_text(pr_text):
    prompt = "generate a very short german twitter post text out of this press release for the ifo institute: " + pr_text
    output_text = generate_response(prompt)
    return output_text


def keyword(pr_text):
    prompt = "generate one simple keyword in english, related to economy and understandable for a child, for a fitting background image for a twitter post to this press release:" + pr_text
    output_text = generate_response(prompt)
    return output_text
