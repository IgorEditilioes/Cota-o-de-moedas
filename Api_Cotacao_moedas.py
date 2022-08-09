import requests

cotacoes = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
cotacoes = cotacoes.json()
dolar = cotacoes['USDBRL']['bid']
euro = cotacoes['EURBRL']['bid']
bitcoin = cotacoes['BTCBRL']['bid']

dolar = float(dolar)
euro = float(euro)
bitcoin = float(bitcoin)
bitcoin = (bitcoin * 1000)

print(f'cotação do dolar: R${dolar:,.3f}')
print(f'cotação do euro: R${euro:,.3f}')
print(f'cotação do bitcoin: R${bitcoin:,.3f}')