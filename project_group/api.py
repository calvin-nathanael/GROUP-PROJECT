import requests
from pathlib import Path

# making an API call to CURRENCY_EXCHANGE_RATE
currency_url = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=SGD&apikey=0I9X3CH0ID27ONE2'
r = requests.get(currency_url)
data = r.json()

def api_function():

    # accessing the data using nested dictionariea
    exchange_rate = float(data['Realtime Currency Exchange Rate']['5. Exchange Rate'])

    # writing the exchange rate into the summary report
    report_path = Path.cwd()/"project_group"/"summary_report.txt"
    with report_path.open(mode="w") as file:
        file.write(f"[REAL TIME CURRENCY CONVERSION RATE] USD1 = SGD{round(exchange_rate, 5)}")

    return exchange_rate