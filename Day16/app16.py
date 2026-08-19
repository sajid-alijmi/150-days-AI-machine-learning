import pandas as pd 

df = pd.read_csv("emplyee_data.csv")
print(df, type(df))



df = pd.read_json("empoyee_data.json")

print(df)