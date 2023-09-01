import requests

api_url = 'https://api.example.com/data'
data_to_send = {
    'key1' : 'value1',
    'key2' : 'value2',
    }

headers = {'Content-Type': 'application/json'}

response = requests.post(api_url, json=data_to_send, headers=headers)

if response.status_code == 200:
    data = response.json()

    print(data)
else:
    print(f'Error: {response.status_code}')

