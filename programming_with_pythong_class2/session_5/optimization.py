#!/usr/bin/env python3

import numpy as np 
import pandas as pd 
from datetime import datetime
import matplotlib.pyplot as plt
import scipy.optimize as sco

mult = 52.1429 #number of weeks per year
#

df = pd.read_csv('StockData.csv', index_col=False)
df = df.iloc[:,0:5] # select number of columns
train_df = df.iloc[int(len(df.index)/5):len(df.index),:]
sample_df = df.iloc[0:int(len(df.index)/5),:]

train_returns_df = train_df.sort_index(ascending=False)
train_returns_df.iloc[:,1:] = train_returns_df.iloc[:,1:].add(1)
for row in range(0,len(train_returns_df.index), +1):
 	train_returns_df.iloc[row,1:] = (train_returns_df.iloc[row,1:]).mul(train_returns_df.iloc[row-1,1:])
print("Graph Returns")
train_returns_df.plot(figsize=(8,5))
plt.savefig("./returns.png")

print("-->Sample Data")
print(sample_df)
print("-->Train Data")
print(train_df)
noc=len(train_df.columns)-1 # total number for index of columns
# print(len(train_df.index))
print("-->Avarage Returns")
print(train_df.mean() * mult) # annualized mean return
# print(train_df.cov() * mult) # annualized covariance matrix

print("-->Select random weights")
weights = np.random.random(noc) # initial random weights
weights /= np.sum(weights) #take weight devide by sum of eights and save 
print(weights)


exp_ret = np.dot(train_df.mean(), weights) * mult #annualized expected return with initial weights
print("-->Expected return with selected weights {}".format(exp_ret))

exp_var = np.dot(weights.T, np.dot(train_df.cov() * mult, weights))
exp_vol = np.sqrt(exp_var)
print("Expected Variance {}".format(exp_var))
print("Expected Volatility {}".format(exp_vol))

# Trying different set of weights 
print("\n\n -->Trying different weights and accumulating returns")
steps = 1000
prets = []
pvols = []
for i in range(steps):
	weights = np.random.random(noc)
	weights /= np.sum(weights)
	exp_ret = np.dot(train_df.mean(), weights) * mult
	prets.append(exp_ret)
	exp_var = np.dot(weights.T, np.dot(train_df.cov() * mult, weights))
	pvols.append(np.sqrt(exp_var))
prets = np.array(prets)
pvols = np.array(pvols)
	

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
print("\n\n -->Getting started with optimization \nMaximize Return/Risk")

def statistics(weights):
	weights = np.array(weights)
	pret = np.dot(train_df.mean(), weights) * mult
	pvol = np.sqrt(np.dot(weights.T, np.dot(train_df.cov() * mult, weights)))
	return(np.array([pret,pvol, pret / pvol]))

def min_sharpe(weights):
	return(-statistics(weights)[2])
cons = ({'type':'eq', 'fun':lambda x: np.sum(x) - 1}) #defining constraints 
bnds = tuple((0, 1) for x in range(noc))
base_weights = noc * [1/noc,] #start with equal weights 

opts = sco.minimize(min_sharpe, base_weights, method='SLSQP', bounds=bnds, constraints=cons)
print("Results of the optimization")
print(opts)
blub = np.delete(np.array(train_df.columns),(0), axis=0)
max_sharp_weights = np.column_stack((blub, opts['x'].T.round(3)))
print("\nSorted list of underlying names and respective weights")
max_sharp_weights = np.flipud(max_sharp_weights[max_sharp_weights[:,1].argsort()])
# max_sharp_weights = np.array(train_df.columns,opts['x'])
print(max_sharp_weights)

print("Statistics - Vol / Return / Sharpe \n{}".format(statistics(opts['x']).round(3)))

print("\nMinimize Risk - Variance")
def min_variance(weights):
	return(statistics(weights)[1] ** 2)

optv = sco.minimize(min_variance, base_weights, method='SLSQP', bounds=bnds, constraints=cons)
print("Results of the optimization")
print(optv)
min_var_weights = np.column_stack((blub, optv['x'].T.round(3)))
print("\nSorted list of underlying names and respective weights")
min_var_weights = np.flipud(min_var_weights[min_var_weights[:,1].argsort()])
# min_var_weights = np.array(train_df.columns,optv['x'])
print(min_var_weights)

print("Statistics - Vol / Return / Sharpe {}".format(statistics(optv['x']).round(3)))

print("-->Efficient Frontier<--")

cons = ({'type':'eq', 'fun':lambda x: statistics(x)[0] - tret},   #New constraints
		{'type':'eq', 'fun':lambda x: np.sum(x) - 1})
bnds = tuple((0, 1) for x in range(noc))

def min_pvol(weights):   #New function to minimize
	return(statistics(weights)[1])

trets = np.linspace(0.0,0.25,50)
tvols =[]
for tret in trets:
	cons = ({'type':'eq', 'fun':lambda x: statistics(x)[0] - tret},{'type':'eq', 'fun':lambda x: np.sum(x) - 1})
	# bnds = tuple((0, 1) for x in range(noc))
	res = sco.minimize(min_pvol, base_weights, method='SLSQP', bounds=bnds, constraints=cons)
	tvols.append(res['fun'])
tvols = np.array(tvols)
front_line = np.column_stack((trets, tvols))
print("Data for Efficient Frontier")
print(front_line)
print("Please check the graph FrontierLine.png")

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
