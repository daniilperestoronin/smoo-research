import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from scipy.optimize import linprog

# a dataset for portfolio optimization and other finance applications.
# It covers 10 years, from January 2006 to December 2016, and comprises a set
# of 52 popular exchange traded funds (ETFs) and the US central bank (FED)
# rate of return

returns = pd.read_csv('./data/returns.csv', index_col=0)

# an assets array of dimension n
assets = np.array(returns.columns)

# a dates array of dimension T
dates = np.array(returns.index)

# a returns matrix of dimension T by n (non-dimensional).
returns = returns.values
T, n = returns.shape

# a volumes matrix of dimension T by n, in dollars
volumes = np.genfromtxt('./data/volumes.csv', delimiter=',')[2:, 1:]

# a prices matrix of dimension T by n, in dollars
prices = np.genfromtxt('./data/prices.csv', delimiter=',')[2:, 1:]

# The probability of a negative return matrix
prob_n_ret = np.genfromtxt('./data/n_prob.csv', delimiter=',')[2:, 1:]

################################################################################
# Graphs
################################################################################

plt.plot(returns)
plt.title('Daily market returns for last 10 years')
plt.xlabel('days')
plt.legend(assets, loc=2, prop={'size': 2})
plt.show()

plt.plot(volumes)
plt.title('Daily market volumes for last 10 years')
plt.xlabel('days')
plt.ylabel('dollars')
plt.legend(assets, loc=2, prop={'size': 2})
plt.show()

plt.plot(prices)
plt.title('Daily market close prices for last 10 years')
plt.xlabel('days')
plt.ylabel('dollars')
plt.legend(assets, loc=2, prop={'size': 2})
plt.show()

plt.plot(prob_n_ret)
plt.title('The probability of a negative return for last 10 years')
plt.xlabel('days')
plt.legend(assets, loc=2, prop={'size': 2})
plt.show()

################################################################################
# Linprog
################################################################################

#####
# Solve in mean
#####

# mean return
m_returns = np.sum(returns, axis=0) / T

# mean probability of a negative return
m_prob_n_ret = np.sum(prob_n_ret, axis=0) / float(T)

alpha = 0.5
gamma = 0.5

vct = list(-alpha * m_returns / np.amax(m_returns) + gamma * m_prob_n_ret / np.amax(m_prob_n_ret))

matrix = [[0 for y in xrange(n)] for x in xrange(n)]
matrix[0] = - m_returns
matrix[1] = [1 for i in xrange(n)]

b = [0 for i in xrange(n)]
b[0] = - 0.1
b[0] = 1

res = linprog(vct, A_ub=matrix, b_ub=b, method='interior-point')

print(res)

#####
# Negative
#####

n_returns = np.amin(returns, axis=0)
n_prob_n_ret = np.amin(prob_n_ret, axis=0)
n_vct = list(-alpha * n_returns / np.amax(n_returns) + gamma * n_prob_n_ret / np.amax(n_prob_n_ret))

matrix = [[0 for y in xrange(n)] for x in xrange(n)]
matrix[0] = - n_returns
matrix[1] = [1 for i in xrange(n)]

b = [0 for i in xrange(n)]
b[0] = - 0.1
b[0] = 1

n_res = linprog(n_vct, A_ub=matrix, b_ub=b, method='interior-point')

print(n_res)

#####
# Positive
#####

p_returns = np.amax(returns, axis=0)
p_prob_n_ret = np.amax(prob_n_ret, axis=0)
p_vct = list(-alpha * p_returns / np.amax(p_returns) + gamma * p_prob_n_ret / np.amax(p_prob_n_ret))

matrix = [[0 for y in xrange(n)] for x in xrange(n)]
matrix[0] = - p_returns
matrix[1] = [1 for i in xrange(n)]

b = [0 for i in xrange(n)]
b[0] = - 0.1
b[0] = 1

p_res = linprog(p_vct, A_ub=matrix, b_ub=b, method='interior-point')

print(p_res)
