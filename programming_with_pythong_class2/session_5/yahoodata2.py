#!/usr/bin/env python3

import numpy as np 
import pandas as pd 
from datetime import datetime
from pandas_datareader import data as web



# Dow Jones Industrial Average Tickers

DJIA = ['^GSPC',    'AAPL',    'AXP',    'BA',    'CAT',    'CSCO',    'CVX',    'KO',    'DD',
  'XOM',    'GE',    'GS',    'HD',    'IBM',    'INTC',    'JNJ',    'JPM',
   'MCD',    'MMM',    'MRK',    'MSFT',    'NKE',    'PFE',    'PG',    'TRV',
    'UNH',    'UTX',    'V',    'VZ',    'WMT',    'DIS']

# Dates

start = datetime(2010, 1, 1)
end = datetime.today()

# Grab data, change to weekly returns and write to CSV

print("Start time", datetime.today().now())  #keep time

x = web.DataReader(DJIA,"yahoo", start, end)['Adj Close']
# x = x.ix['Adj Close']

df = pd.DataFrame(x)
# df = df.sort_index(ascending=False)


df = df.resample('W-FRI').last().sort_index(ascending=False) #changing data to weekly
print(df)
for row in range(len(df)-1):
    df.iloc[row] = df.iloc[row].div(df.iloc[row+1]) #return
df = df.iloc[:-1]
df = np.log(df)  #taking log return

df.to_csv('StockData.csv', encoding='utf-8') #write to CSV


print("End Time: ", datetime.today().now())