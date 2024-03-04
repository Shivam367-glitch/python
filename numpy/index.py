import numpy as np

# print(dir(numpy))
arr=np.array([1,23,4,5,6,3])
a=[32,32,33]
arr=np.append(a,arr)
print(np.__version__)
print(type(arr))
print(arr.ndim)
for x in arr:
      print(x,end=" ")

