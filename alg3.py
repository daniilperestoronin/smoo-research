import numpy as np
import pandas as pd

returns = pd.read_csv('./data/returns.txt', index_col=0)
assets = np.array(returns.columns)
dates = np.array(returns.index)
returns = returns.values
T, n = returns.shape
volumes = np.genfromtxt('./data/volumes.txt', delimiter=',')[2:, 1:]
prices = np.genfromtxt('./data/prices.txt', delimiter=',')[2:, 1:]

print(returns)
print(assets)
print(dates)

print(volumes)
print(volumes)
