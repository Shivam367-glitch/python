import pandas as pd

data = {'a': 10, 'b': None, 'c': 30, 'd': 40, 'e': 50}
s = pd.Series(data,index=["Shivam","Aman","Kolkata"])

# . Handling Missing Data:
ss=s.dropna()
# print(ss)

import matplotlib.pyplot as plt

ss.plot()
plt.show()

# Mean
# result = s.mean()

# Standard deviation
# result = s.std()

# Maximum value
# result = s.max()

# Minimum value
result = s.min()

print(result)



