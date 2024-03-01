import math
import sys

min_int_value = -sys.maxsize - 1
print(min_int_value)

list =[10,20,1,211,221,32,1,22,-1]

for x in list:
    min_int_value=max(min_int_value,x)


print(min_int_value)


print(min(list))