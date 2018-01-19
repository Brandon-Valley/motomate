#https://github.com/sammchardy/python-binance
from binance.client import Client

api_key = '4jRVOPdfafcrVP5Ke3DL1g4RKleTTlwirQDrlADivdKjZSaUHsXlZ6XMjfXS95oZ'
api_secret = 'xnvyR7mq22DlO4PnUqa71OWwGTzdddHhapqpzf0iwtQGSA1VRmtLdp92xpUdrfkE' 

client = Client(api_key, api_secret)

# get all symbol prices
prices = client.get_all_tickers()
print(prices)
