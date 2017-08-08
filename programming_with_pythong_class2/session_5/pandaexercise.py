#!/usr/bin/env python3

import pandas as pd
import matplotlib
# matplotlib.use("Agg")

broken_df = pd.read_csv("./comptagevelo20162.csv", encoding='latin1', parse_dates=['Date'], dayfirst=True, index_col='Date')

broken_df["Berri1"].plot()




if __name__ == '__main__':
	print(broken_df)