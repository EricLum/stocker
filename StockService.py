from urllib import request
import json
from config import apikey

class StockService:
    def __init__(self, symbol, apikey):
        self.apikey = apikey
        self.symbol = symbol
        url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={self.symbol}&apikey={self.apikey}"
        with request.urlopen(url) as response:
           myjson = json.loads(response.read())
           print(myjson['Meta Data']['2. Symbol'])
           timeseries = myjson['Time Series (Daily)']
           for time in timeseries:
               myDataPoint = StockDataPoint(time, timeseries[time])
               myDataPoint.print()




class StockDataPoint:
    def __init__(self, date, datapoint):
        self.high = datapoint['2. high']
        self.low = datapoint['3. low']
        self.date = date

    def print(self):
        sentence = f'On {self.date}, your stock had a high of {self.high} and a low of {self.low}'
        print(sentence)


service = StockService('AAPL', apikey)

