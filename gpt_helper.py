import openai

# Configure your OpenAI GPT API key
openai.api_key = 'YOUR_OPENAI_API_KEY'

def generate_gpt_response(text):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=text,
        max_tokens=150
    )
    return response.choices[0].text.strip()
