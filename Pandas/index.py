import pandas as pd

mydataset = {
  'name': ["Shivam", "Akash", "Pawan"],
  'passings': [31, 17, 12]
}

myvar = pd.DataFrame(mydataset)
print(myvar.loc[[0, 1]])  

# get row 
# print(myvar.loc[1])

# get mulitple row 




