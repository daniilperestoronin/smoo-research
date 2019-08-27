import numpy as np

try:
  import pandas as pd

  returns = pd.read_csv('returns.txt', index_col=0)
  assets = np.array(returns.columns)
  dates = np.array(returns.index)
  returns = returns.as_matrix()
except ImportError:
  returns = np.genfromtxt('returns.txt', delimiter=',')[1:, 1:]
  with open('returns.csv') as f:
    lines = f.readlines()
  assets = np.array(lines[0][:-1].split(',')[1:])
  dates = np.array([line[:10] for line in lines[1:]])
T, n = returns.shape
volumes = np.genfromtxt('volumes.txt', delimiter=',')[2:, 1:]
prices = np.genfromtxt('prices.txt', delimiter=',')[2:, 1:]
