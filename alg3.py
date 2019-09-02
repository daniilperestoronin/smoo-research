import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from scipy.optimize import linprog

# a dataset for portfolio optimization and other finance applications.
# It covers 10 years, from January 2006 to December 2016, and comprises a set
# of 52 popular exchange traded funds (ETFs) and the US central bank (FED)
# rate of return

returns = pd.read_csv('./data/returns.txt', index_col=0)

# an assets array of dimension n
assets = np.array(returns.columns)

# a dates array of dimension T
dates = np.array(returns.index)

# a returns matrix of dimension T by n (non-dimensional).
returns = returns.values
T, n = returns.shape

# a volumes matrix of dimension T by n, in dollars
volumes = np.genfromtxt('./data/volumes.txt', delimiter=',')[2:, 1:]

# a prices matrix of dimension T by n, in dollars
prices = np.genfromtxt('./data/prices.txt', delimiter=',')[2:, 1:]

# The probability of a negative return matrix
prob_n_ret = np.empty([T, n])

for i in xrange(T):
    prob_n_ret[i] = np.sum(np.array(returns[:i, :]) <= 0, axis=0) / float(i + 1)

print(prob_n_ret)

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

# mean return
m_returns = np.sum(returns, axis=0) / T

# The probability of a negative return
n_exp = np.sum(np.array(returns) <= 0, axis=0) / float(T)

alpha = 0.5
gamma = 0.5

vct = list(-alpha * m_returns + gamma * n_exp)

matrix = [[0 for y in xrange(n)] for x in xrange(n)]
matrix[0] = m_returns

b = [0 for i in xrange(n)]
b[0] = 100000

res = linprog(vct, A_eq=matrix, b_eq=b, method='interior-point')

print(res)
