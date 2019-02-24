#!/usr/bin/env python3

from datetime import datetime
from pandas_datareader import data as web

stockname = ['BIV']
now = datetime.now()

currentprice = web.DataReader(stockname,"yahoo", now, now)['Adj Close']

if __name__ == "__main__":
    print(currentprice)