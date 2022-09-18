import requests

url = "https://api.covid19api.com/country/brazil"

req = requests.get(url)

dados = req.json()

for i in range(len(dados)):
    if dados[i]['Confirmed'] == 1:
        data = dados[i]['Date']

print(data)