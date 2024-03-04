import numpy as np

arr = np.array([6, 7, 8, 9])

x = np.searchsorted(arr, [1,2,910])

print(x)