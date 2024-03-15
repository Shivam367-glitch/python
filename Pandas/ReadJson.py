import pandas as pd

file_path = r'C:\Users\SHIVAM\Desktop\Python\Pandas\data.json'
myvar=pd.read_json(file_path)


print(myvar.to_string())