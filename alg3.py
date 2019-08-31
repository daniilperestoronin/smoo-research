import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

returns = pd.read_csv('./data/returns.txt', index_col=0)
assets = np.array(returns.columns)
dates = np.array(returns.index)
returns = returns.values
T, n = returns.shape
volumes = np.genfromtxt('./data/volumes.txt', delimiter=',')[2:, 1:]
prices = np.genfromtxt('./data/prices.txt', delimiter=',')[2:, 1:]

################################################################################
# Graphs
################################################################################

print(assets)

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
