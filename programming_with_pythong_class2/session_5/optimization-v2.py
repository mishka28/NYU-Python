#!/usr/bin/env python3

import numpy as np 
import pandas as pd 
from datetime import datetime
import matplotlib.pyplot as plt
import scipy.optimize as sco

mult = 52.1429 #number of weeks per year
dataframe = pd.read_csv('StockData.csv', index_col=False)

def split_data(dataframe):

	df = dataframe.iloc[:,0:5] # select number of columns
	trn_df = df.iloc[int(len(df.index)/5):len(df.index),:]
	sample_df = df.iloc[0:int(len(df.index)/5),:]
	return(trn_df,sample_df)

trn_df = split_data(dataframe)[0]

def graph_ret(dataframe, location):
	trn_ret_df = dataframe.sort_index(ascending=False)
	trn_ret_df.iloc[:,1:] = trn_ret_df.iloc[:,1:].add(1)
	for row in range(0,len(trn_ret_df.index), +1):
 		trn_ret_df.iloc[row,1:] = (trn_ret_df.iloc[row,1:]).mul(trn_ret_df.iloc[row-1,1:])
	trn_ret_df.plot(figsize=(8,5))
	plt.savefig(location)
	return()

noc=len(trn_df.columns)-1 # total number for index of columns

def basic_ret(dataframe):# annualized mean return
	weights = np.random.random(noc) # initial random weights
	weights /= np.sum(weights) #take weight devide by sum of eights and save 
	
	exp_ret = np.dot(trn_df.mean(), weights) * mult #annualized expected return with initial weights
	exp_var = np.dot(weights.T, np.dot(trn_df.cov() * mult, weights))
	exp_vol = np.sqrt(exp_var)
	return(exp_var, exp_vol, exp_ret)

# Trying different set of weights 
def simulation(dataframe, steps):
	prets = []
	pvols = []
	for i in range(steps):
		weights = np.random.random(noc)
		weights /= np.sum(weights)
		exp_ret = np.dot(trn_df.mean(), weights) * mult
		prets.append(exp_ret)
		exp_var = np.dot(weights.T, np.dot(trn_df.cov() * mult, weights))
		pvols.append(np.sqrt(exp_var))
	prets = np.array(prets)
	pvols = np.array(pvols)
	return(prets, pvols)

prets, pvols = simulation(trn_df,1000)[0:3]
exp_vol, exp_ret = basic_ret(trn_df)[1:3]
plt.figure(figsize=(8,4))
plt.scatter(pvols,prets, c=prets / pvols, marker ="o")
plt.plot(exp_vol,exp_ret, 'r*', markersize=15.0)
plt.grid(True)
plt.xlabel("Expected Volatility: Risk")
plt.ylabel("Expected Return")
plt.colorbar(label = "Sharpe ratio")
plt.savefig("./scatterplot.png")
print("Please see the scatterplot.png")

# Maximixe return/Risk 

def statistics(weights):
	weights = np.array(weights)
	pret = np.dot(trn_df.mean(), weights) * mult
	pvol = np.sqrt(np.dot(weights.T, np.dot(trn_df.cov() * mult, weights)))
	return(np.array([pret,pvol, pret / pvol]))

def min_sharpe(weights):
	return(-statistics(weights)[2])
def min_variance(weights):
	return(statistics(weights)[1] ** 2)
def min_pvol(weights):   #New function to minimize
	return(statistics(weights)[1])

base_weights = noc * [1/noc,]	
cons = ({'type':'eq', 'fun':lambda x: np.sum(x) - 1}) #defining constraints 
bnds = tuple((0, 1) for x in range(noc))
blub = np.delete(np.array(trn_df.columns),(0), axis=0)

opts = sco.minimize(min_sharpe, base_weights, method='SLSQP', bounds=bnds, constraints=cons)
max_sharp_weights = np.column_stack((blub, opts['x'].T.round(3)))
max_sharp_weights = np.flipud(max_sharp_weights[max_sharp_weights[:,1].argsort()])
print(max_sharp_weights)

optv = sco.minimize(min_variance, base_weights, method='SLSQP', bounds=bnds, constraints=cons)
min_var_weights = np.column_stack((blub, optv['x'].T.round(3)))
min_var_weights = np.flipud(min_var_weights[min_var_weights[:,1].argsort()])
print(min_var_weights)

cons = ({'type':'eq', 'fun':lambda x: statistics(x)[0] - tret},   #New constraints
		{'type':'eq', 'fun':lambda x: np.sum(x) - 1})

trets = np.linspace(0.0,0.25,50)
tvols =[]
for tret in trets:
	res = sco.minimize(min_pvol, base_weights, method='SLSQP', bounds=bnds, constraints=cons)
	tvols.append(res['fun'])
tvols = np.array(tvols)
front_line = np.column_stack((trets, tvols))

plt.figure(figsize=(8,4))
plt.scatter(pvols,prets, c=prets / pvols, marker ="o")
plt.scatter(tvols,trets, c=trets / tvols, marker ="x")
plt.plot(statistics(opts['x'])[1],statistics(opts['x'])[0], 'r*', markersize=15.0)
plt.plot(statistics(optv['x'])[1],statistics(optv['x'])[0], 'y*', markersize=15.0)
plt.grid(True)
plt.xlabel("Expected Volatility: Risk")
plt.ylabel("Expected Return")
plt.colorbar(label = "Sharpe ratio")
plt.savefig("./FrontierLine.png")
