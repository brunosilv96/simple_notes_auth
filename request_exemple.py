from pprint import pprint
import requests

nome: str = 'Bruniele'
url: str = f'https://servicodados.ibge.gov.br/api/v2/censos/nomes/{nome}'

response = requests.get(url, params={'groupBy': 'UF'}, timeout=None)

try:
    response.raise_for_status()
except requests.HTTPError as error:
    print(f'Erro na requisição: {error}')
    print(f'Status Code: {error.response.status_code} | Error: {error.response.reason}')
else:
    response = response.json()
    pprint(response)
