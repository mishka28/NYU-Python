#!/usr/bin/env python3

import pandas as pd 
from datetime import datetime
from pandas_datareader import data


print("Start time", datetime.today().now())

# Grab Data

def get_data(symbol, start_date, end_date):

    dat = data.DataReader(symbol, "yahoo", start_date, end_date)

    dat["Ratio"] = dat["Adj Close"] / dat["Close"]

    dat["Open"] = dat["Open"] * dat["Ratio"]
    dat["High"] = dat["High"] * dat["Ratio"]
    dat["Low"] = dat["Low"] * dat["Ratio"]
    dat["Close"] = dat["Close"] * dat["Ratio"]

    return(dat)

# Dow Jones Industrial Average Tickers

DJIA = ['AAPL',    'AXP',    'BA',    'CAT',    'CSCO',    'CVX',    'KO',    'DD',
#  'XOM',    'GE',    'GS',    'HD',    'IBM',    'INTC',    'JNJ',    'JPM',
 #   'MCD',    'MMM',    'MRK',    'MSFT',    'NKE',    'PFE',    'PG',    'TRV',
    'UNH',    'UTX',    'V',    'VZ',    'WMT',    'DIS']

# Dates

start = datetime(2017, 7, 1)
end = datetime.today()
index = pd.date_range(start,end, freq='D')
#Grab and Save Data

#fh = open("./StockData.csv","a")

# DX=pd.DataFrame(index = index, columns=DJIA)
#print(DX)
#DX.columns=[DJIA]
#print(DX)


# x = get_data(DJIA, start, end)

x = data.DataReader(DJIA,"yahoo", start, end)
x = x.ix['Close']

DF = pd.DataFrame(x)

DF.to_csv('StockData.csv', encoding='utf-8')
    #DF.columns=[ticker]
    #print(DF)
    #DF.to_csv("./StockData.csv", sep=',', mode='a')
#fh.write(DF)
# fh.close()

# data = broken_df = pd.read_csv("./StockData.csv")

# print(data)

print("End Time: ", datetime.today().now())