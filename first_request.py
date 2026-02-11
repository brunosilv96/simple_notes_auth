import requests

try:
    url: str = 'http://httpbin.org/get'

    response = requests.get(url)

    print(response.json())

except Exception as error:
    print(f'Erro no engano: {error}')
    
