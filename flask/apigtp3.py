import requests

api_key = 'your api key'

endpoint = 'https://api.openai.com/v1/engines/davinci-codex/completions'

headers = {
    'Content-Type': 'application/json',
    'Authorization' : f'Bearer {api_key}'
}

data = {

    'prompt': 'Translate the following English text to French: "{text}" ',
    #respnse length
    'max_tokens': 50, 
}

response = requests.post(endpoint, json=data, headers=headers)

if response.status_code == 200:
    result = response.json()
    generated_text = result['choices'][0]['text']
    print(generated_text)
else:
    print(f'Error: {response.status_code}')
