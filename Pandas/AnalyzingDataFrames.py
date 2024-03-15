import pandas as pd

file_path = r'C:\Users\SWEETA\Desktop\Python\Pandas\people.csv'
myvar = pd.read_csv(file_path)

# get info about data present in file and 
print(myvar.info())