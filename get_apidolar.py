import requests
import json
import pandas as pd

def getdata(url):
    r=requests.get(url)
    return r.text

database = getdata('https://economia.awesomeapi.com.br/last/USD-BRL')

corrigido = json.loads(database)

#print(corrigido['USDBRL']['high'])

teste = pd.read_json(database)

print(teste['high'])
