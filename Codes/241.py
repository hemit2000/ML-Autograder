import numpy as np

data1 = [1,2,3,4,5]
data2 = [2,4,6,8,10]

correlation = np.corrcoef(data1, data2)[0][1]
print(correlation)
