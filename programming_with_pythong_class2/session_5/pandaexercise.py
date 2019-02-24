#!/usr/bin/env python3

import pandas as pd
import matplotlib
# matplotlib.use('Agg')
import matplotlib.pyplot as plt 

# matplotlib.use("Agg")
# import pylab as p



broken_df = pd.read_csv("./comptagevelo20162.csv", encoding='latin1', parse_dates=['Date'], dayfirst=True, index_col='Date')

# p.plot(broken_df["Berri1"])
# p.show()
broken_df["Berri1"].plot()
# broken_df.plot()
# plt.show()

plt.savefig("./graph.png")


# if __name__ == '__main__':
	# print(broken_df)