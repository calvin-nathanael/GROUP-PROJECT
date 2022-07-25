import requests

# making an API call to FX_WEEKLY 
currency_url = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=SGD&apikey=0I9X3CH0ID27ONE2'
r = requests.get(currency_url)
data = r.json()

def mean_forex_closing_price():

    # accessing the data using nested dictionariea
    return data['Realtime Currency Exchange Rate']['5. Exchange Rate']
