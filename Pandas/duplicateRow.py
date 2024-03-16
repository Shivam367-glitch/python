import pandas as pd


file_path=r'C:\Users\SHIVAM\Desktop\Python\Pandas\people.csv'

my_var=pd.read_csv(file_path)

# print(my_var.duplicated().to_string())

# Removing Duplicates


my_var.drop_duplicates()








