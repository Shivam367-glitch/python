import matplotlib.pyplot as plt
import numpy as np


x1=[1,2,3,4]
y1 = np.array([3, 8, 1, 10])

x2=[11,12,13,40]
y2 = np.array([6, 2, 7, 11])

plt.plot(x1,y1)
plt.plot(y1,y2)

plt.show()