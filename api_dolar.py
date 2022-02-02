import requests
import json

cotacoes = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
cotacoes = cotacoes.json()
cotacao_dolar = cotacoes['USDBRL']["bid"]
cotacao_euro = cotacoes['EURBRL']["bid"]
cotacao_bitcoin = cotacoes['BTCBRL']["bid"]

print(f"\n Cotação do Real Brasileiro/Dólar Americano (US$): R$ {cotacao_dolar}")
print(f"\n Cotação do Real Brasileiro/Euro (€): R$ {cotacao_euro}")
print(f"\n Cotação do Real Brasileiro/Bitcoin (BTC): R$ {cotacao_bitcoin}")
print("\n Cotações sem formatação: \n",cotacoes)