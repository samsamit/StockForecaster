# Algoritmin tarkoitus
Algoritmin tarkoituksena on ensinnäkin nostaa esille osakkeista ne, joissa on Momentumia/ jotka ovat Trendaamassa ja toisekseen tukea päätöksen tekoa. Osakemarkkinat ovat erityisesti lyhyellä aikajänteellä "tunteellisia" tarkoittaen sitä, että ihmiset yleensä joko ostavat koska eivät halua jäädä jälkeen tai panikoivat jolloin osakkeita myydään ehkä turhaankin. 
Algolla pyritään luomaan pohjaa sille, että näitä "tunteita" pystytään tavalla tai toisella ennakoimaan sekä mahdollisimman hyvin "poistamaan" omat tunteet päätöksenteosta.
Jotta ennakointia pystytään tekemään, niin on oltava tarpeeksi paljon ja tarpeeksi vahvoja osto- tai myyntisignaaleja.

# Momentum/ Trendit - investointi
Momentum tai Trending investoinneissa tarkoituksena on ns. hypätä nousijoiden kelkkaan. Esimerkiksi osake on noussut x ajan ja tekniseen analyysiin perustuen tilanne ei ole muuttumassa, niin tätä osaketta voisi ostaa. Sitten kun vauhti on hiljentymässä, niin voi osaketta myydä osittain tai kokonaan pois ja hypätä uuden osakkeen kelkkaan.

# Tekninen analyysi
Tekninen analyysi on yksi analysoinnin menetelmistä, joita käytetään kun analysoidaan osakkeita. Tekninen analyysi perustuu mm. osakkeen hintaan (jollakin aikavälillä), volatiliteettiin (kuinka paljon osaketta myydään/ostetaan) ja moniin muihin lukuihin. Alla on linkki, jossa teknistä analyysia ja erilaisia analyysimenetelmiä on avattu.

https://www.investopedia.com/terms/t/technical-analysis-of-stocks-and-trends.asp

# RSI - Relative Strength Index
RSI:in tarkoitus on saada selville, onko osake "yliostettu vai -myyty". 50 = osake on vakaa, 70 tai yli = yliostettu, 30 tai alle = ylimyyty.

# ROC - Rate of Change
Kuinka nopeasti osakkeen hinta muuttuu x ajassa. 

# McClellan Oscillator
Osakkeiden nousut ja laskut. Tyypillisesti seurataan koko markkinaa. Eli montako osaketta nousee ja laskee jne. Tähän oma tvisti ainoastaan.

# EMA
Exponential Moving Average - Sama kuin SMA (Simple Moving Average), mutta antaa enemmän painoarvoa viimeisimmille muutoksille. 





# Koodin pätkä

import numpy as np
import pandas as pd
import yfinance as yf
from get_all_tickers import get_tickers as gt
import shutil
import os
import requests
import xlsxwriter
import math

shutil.rmtree(" ")
os.mkdir(" ")

tickers = gt.get_tickers_filtered(mktcap_min=150000, mktcap_max=10000000)
print("The amount of stocks chosen to observe: " + str(len(tickers)))

Stock_Failure = 0
Stocks_Not_Imported = 0

i=0
while (i < len(tickers)) and (Amount_of_API_Calls < 1800):
    try:
        stock = tickers[i]  # Gets the current stock ticker
        temp = yf.Ticker(str(stock))  # Instantiate the ticker as a stock with Yahoo Finance
        Hist_data = temp.history(period="max")  # Tells yfinance what kind of data we want about this stock (In this example, all of the historical data)
        Hist_data.to_csv(" ")  # Saves the historical data in csv format for further processing later
        time.sleep(2)  # Pauses the loop for two seconds so we don't cause issues with Yahoo Finance's backend operations
        Amount_of_API_Calls += 1
        Stock_Failure = 0
        i += 1  # Iteration to the next ticker
    except ValueError:
        print("Yahoo Finance Back-end Error, Attempting to Fix")  # An error occurred on Yahoo Finance's back-end. We will attempt to retreive the data again
        if Stock_Failure > 5:  # Move on to the next ticker if the current ticker fails more than 5 times
            i+=1
            Stocks_Not_Imported += 1
        Amount_of_API_Calls += 1
        Stock_Failure += 1
print("The amount of stocks we successfully imported: " + str(i - Stocks_Not_Imported))