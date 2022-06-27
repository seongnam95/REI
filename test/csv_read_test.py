import pandas as pd
import numpy as np

data = pd.read_csv('../test/seoul.csv', sep="|")

cols = ''
for i in data.columns:
    cols += '`%s`, ' % i

print(cols)
#
# for i in np.array_split(data, 10000):
#     print(i)
