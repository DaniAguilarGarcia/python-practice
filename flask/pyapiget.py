#handling an API with python, generic
#request.get() method to make a GET request to the API
import requests

api_url = 'https://api.example.com/data'
response = requests.get(api_url)

if response.status_code == 200: 
    data = response.json()

    print(data)
else:
    print(f'Erros:{response.status_code}')

