import requests as r
import datetime as dt
import csv
from PIL import Image
from IPython.display import display
from urllib.parse import quote

confirmado = 0
obitos = 1
recuperado = 2
ativos =3
data =4
url = "https://api.covid19api.com/dayone/country/brazil"
resp = r.get(url)

rawData = resp.json()
finalData = []

for obs in rawData[:365]:
    finalData.append([obs['Confirmed'], obs['Deaths'], obs['Recovered'], obs['Active'], obs['Date']])

finalData.insert(0, ['Confirmados', 'Obitos', 'Recuperados', "Ativos", "Data"])

for i in range(1,len(finalData)):
    finalData[i][data] = finalData[i][data][:10]

with open("brasil-covid.csv", "w", encoding="utf-8") as file:
    write = csv.writer(file)
    write.writerows(finalData)

for i in range(1,len(finalData)):
    finalData[i][data] = finalData[i][data] = dt.datetime.strptime(finalData[i][data],"%Y-%m-%d")

def getDatasets(y, labels):
    if type(y[0]) == list:
        datasets = []
        for i in range(len(y)):
            datasets.append({
                'label': labels[i],
                'data': y[i]
            })
        return datasets
    else:
        return [
            {
                'label': labels[0],
                'data': y
            }
        ]

def setTitle(title = ""):
    if title != "":
        display = 'true'
    else:
        display = 'false'
    return {
        'title': title,
        'display': display
    }

def createChart(x, y, labels, kind='bar', title= ''):
    datasets = getDatasets(y, labels)
    options = setTitle(title)

    chart = {
        'type': kind,
        'data': {
            'labels': x,
            'datasets': datasets
        },
        'options': options
    }
    return chart

def getApiChart(chart):
    urlBase = "https://quickchart.io/chart"
    resp = r.get(f"{urlBase}?c={str(chart)}")
    return resp.content

def saveImage(path, content):
    with open(path, "wb") as image:
        image.write(content)

def displayImage(path):
    imgPil = Image.open(path)
    display(imgPil)

yData1 = []
for obs in finalData[1::10]:
    yData1.append(obs[confirmado])

yData2 = []
for obs in finalData[1::10]:
    yData2.append(obs[recuperado])

labels = ['Confirmados', 'Recuperados']

x = []
for obs in finalData[1::10]:
    x.append(obs[data].strftime('%d/%m/%Y'))

chart = createChart(x, [yData1,yData2], labels, title='Grafico confirmados e recuperados')
chartContent = getApiChart(chart)
saveImage('MeuPrimeiroGrafico.png', chartContent)
displayImage('MeuPrimeiroGrafico.png')

def getApiQrcode(link):
    text = quote(link)
    url_base = 'https://quickchart.io/qr'
    resp = r.get(f'{url_base}?text={text}')
    return resp.content

urlBase = "https://quickchart.io/chart"
link = f"{urlBase}?c={str(chart)}"
saveImage("qrCode.png",getApiQrcode(link))
displayImage("qrCode.png")
