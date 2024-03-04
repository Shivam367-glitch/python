import numpy as np

arr=np.array([1,2,34,5,6,7,32])
xx=arr.view()
xx[2]=-1
x=arr.copy()
x[3]=-1
arr[0]=0
print(arr.dtype)
print(x)
print(xx)
print(arr)

