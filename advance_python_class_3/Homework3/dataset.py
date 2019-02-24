#!/usr/bin/env python3
import matplotlib
matplotlib.use('Agg')

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


dataset = pd.read_csv('CPI_Data.csv')

#replace empty spaces in column names
dataset.columns = [c.replace(' ', '_') for c in dataset.columns]

Columns = list(dataset)

def clean_data(dataframe):

	dataframe.drop(['Country_Code','Indicator_Code','Common_Reference_Period', 'Unnamed:_114'], axis = 1, inplace=True)
	dataframe = dataframe.drop(dataframe.index[dataframe.Attribute == 'Reference Period'])
	dataframe = dataframe.drop(dataframe.index[dataframe.Attribute == 'Status'])
	dataframe = dataframe.drop(dataframe.index[dataframe['Indicator_Name'].str.contains("Percentage change")])
	dataframe = dataframe.drop(dataframe.index[dataframe['Indicator_Name'].str.contains("Harmonized")])
	dataframe.drop(['Attribute'], axis = 1, inplace=True)
	dataframe.drop(['Indicator_Name'], axis = 1, inplace=True)
	dataframe = dataframe.groupby(['Country_Name']).agg(lambda x: x.astype(float).sum())
	dataframe = dataframe.transpose()
	dataframe.dropna(axis=1, how='any', inplace = True)	
	return(dataframe)

dataset = clean_data(dataset)

dataset.to_csv('CleanedCPIdata.csv', encoding='utf-8') #write to CSV

#graphing normilized data -----
(dataset.div(dataset.iloc[0,:])).plot(figsize=(8,5))
plt.savefig("./CPIgraphBefore.png")
plt.clf()


#Dropping countries ---------
dataset.drop(['Brazil','Colombia','Israel','New Zealand', 'Mexico', 'Indonesia', 'Australia', 'Canada'], axis = 1, inplace=True)
dataset.to_csv('FinalCPIdata.csv', encoding='utf-8') #write to CSV

(dataset.div(dataset.iloc[0,:])).plot(figsize=(8,5))
plt.savefig("./CPIgraphAfter.png")
plt.clf()

dataset.mean().plot(kind='bar', figsize=(8,9), title='Bar Char - Average CPI')
plt.savefig("./CPIbarchar.png")
plt.clf()

# Finding change mean and std --------
CPIchange = np.log(dataset / dataset.shift(1))
CPIchange = pd.DataFrame(CPIchange)
	

(CPIchange.mean() * 4).plot(kind='bar', figsize=(8,9), title='Bar Char - Mean Returns')
plt.savefig("./Meansbarchar.png")
plt.clf()


CPIchange.plot.box(vert=False, figsize=(9,6), showfliers=False, title = 'Mean confidence interval', grid=True)
plt.savefig("./CPIchangeboxplot.png")
plt.clf()

