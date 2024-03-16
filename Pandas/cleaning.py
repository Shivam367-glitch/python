import pandas as pd
file_path = r'C:\Users\SHIVAM\Desktop\Python\Pandas\people.csv'

my_var=  pd.read_csv(file_path)

# remve empty in data Frames
# new_df=my_var.dropna()


my_var["Age"].fillna(12,inplace=True)

print(my_var.to_string())


