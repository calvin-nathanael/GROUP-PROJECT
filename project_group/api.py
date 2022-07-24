import requests

currency_url = 'https://www.alphavantage.co/query?function=FX_WEEKLY&from_symbol=USD&to_symbol=SGD&apikey=0I9X3CH0ID27ONE2'
r = requests.get(currency_url)
data = r.json()

