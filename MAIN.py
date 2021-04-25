from GetCalculations import GetStockRsi
from util import listToString
import yfinance as yf
# List of all stocks to be gathered
stocks = [
    "MSFT",
    "AAPL",
    "GOOG"
]
# initialize data array
mainData = {}
# generate ticker data object
tickers = yf.Tickers(listToString(stocks))
# loop trough all wanted tickers
for stock in stocks:
    # create array for specified ticker data
    mainData[stock] = {}
    # get stock history from ticker
    stockHistory = tickers.tickers[stock].history(start="2021-01-01", end="2021-04-30")
    # get stocks rsi and pass it to the data array
    mainData[stock]['rsi'] = GetStockRsi(stockHistory)


print(mainData)
