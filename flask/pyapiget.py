#handling an API with python, generic

import requests

api_url = 'https://api.example.com/data'
response = requests.get(api_url)

if response.status_code == 200: 
    data = response.json()

    print(data)
else:
    print(f'Erros:{response.status_code}')

