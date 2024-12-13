import pandas as pd
import numpy as np
import collections

df = pd.read_csv("input.01.day01", sep="   ", header=None)
data = df.to_numpy()
l1 = np.sort(data[:, 0])
l2 = np.sort(data[:, 1])
print(np.sum(np.abs(l1 - l2)))

count = collections.Counter(l2)

s = 0
for v in l1:
    if v in count:
        s += v * count[v]
print(s)
