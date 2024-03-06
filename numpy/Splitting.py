# import numpy as np

# arr = np.array([1, 2, 3, 4, 5, 6])

# newarr = np.array_split(arr, 3)

# print(newarr)44


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

filtered_arr = list(filter(lambda x: x % 2 == 0, arr))  # Filters even numbers

print(filtered_arr)