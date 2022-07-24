from calendar import week
import requests

# making an API call to FX_WEEKLY 
currency_url = 'https://www.alphavantage.co/query?function=FX_WEEKLY&from_symbol=USD&to_symbol=SGD&apikey=0I9X3CH0ID27ONE2'
r = requests.get(currency_url)
data = r.json()

def mean_forex_closing_price():

    # creating total_closing variable to find total closing price
    total_closing = 0

    # using for loop, assigned the dates, and the nested dictionary to date & prices respectively
    for date, prices in data['Time Series FX (Weekly)'].items():

        # accumulating the closing prices into the total_closing price variable
        total_closing += float(prices['4. close'])

    # returning the average
    return total_closing / len(data['Time Series FX (Weekly)'])
