import requests

url = "https://swapi.dev/api/people/4/"

req = requests.get(url)

dados = req.json()

nome = dados['name']
height = dados['height']
mass = dados['mass']
anoNascimento = dados['birth_year']

print(f"Dados do Darth Vader vindo de uma API: Nome:{nome}, Altura: {height}, Massa: {mass}, Ano de Nascimento: {anoNascimento}")