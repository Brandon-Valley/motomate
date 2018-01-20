#https://github.com/sammchardy/python-binance
# klines stuff:  https://sammchardy.github.io/binance/2018/01/08/historical-data-download-binance.html
from binance.client import Client

api_key = '4jRVOPdfafcrVP5Ke3DL1g4RKleTTlwirQDrlADivdKjZSaUHsXlZ6XMjfXS95oZ'
api_secret = 'xnvyR7mq22DlO4PnUqa71OWwGTzdddHhapqpzf0iwtQGSA1VRmtLdp92xpUdrfkE' 

client = Client(api_key, api_secret)

# get all symbol prices
prices = client.get_all_tickers()
print(prices)
