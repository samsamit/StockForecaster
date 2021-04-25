import yfinance as yf

stocks = [
    "MSFT",
    "AAPL",
    "GOOG"
]


def listToString(s):

    # initialize an empty string
    str1 = ""

    # traverse in the string
    for ele in s:
        str1 += ele + ' '

    # return string
    return str1


tickers = yf.Tickers(listToString(stocks))
for stock in stocks:
    msg = 'Fifty day average for ' + stock + ': '
    value = tickers.tickers[stock].info['fiftyDayAverage']
    print(msg + str(value))
