from stockstats import StockDataFrame as Sdf


def GetStockRsi(stockData):
    try:
        # Gets StockDataFrame from wanted stock (used to get wanted calculations)
        calculatedData = Sdf.retype(stockData)
        # Gets wanted calculation from StockDataFrame
        data = calculatedData['rsi_12']
        return data
    except:
        print("Something went wron calculating rsi")
