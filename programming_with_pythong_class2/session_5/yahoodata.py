#!/usr/bin/env python3



import pandas as pd 
from datetime import datetime
from pandas_datareader import data
# if __name__ == '__main__':
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

DJIA = ['AAPL',	'AXP',	'BA',	'CAT',	'CSCO',	'CVX',	'KO',	'DD',
	'XOM',	'GE',	'GS',	'HD',	'IBM',	'INTC',	'JNJ',	'JPM',
	'MCD',	'MMM',	'MRK',	'MSFT',	'NKE',	'PFE',	'PG',	'TRV',
	'UNH',	'UTX',	'V',	'VZ',	'WMT',	'DIS']

# Dates

start = datetime(2010, 1, 1)
end = datetime.today()

#Grab and Save Data

fh = open("StockData","w+")

for ticker in DJIA:
	DF = get_data(ticker, start, end)
	
	for i,date in enumerate(DF.index):
		fh.write("%s,%.2f,%d\n" % (date.strftime("%Y%n%d"),DF["Open"][i],DF["High"][i]) )




fh.close()
print("End Time: ", datetime.today().now())

