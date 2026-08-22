import pandas as pd

df = pd.read_csv("employer_data.csv")

df.isnull()
df.isna
df.isnull().sum()
df.dropna()

df.dtypes
df2 = df.copy()

df2 = df2.fillna(0)
df2 = df2["Age"].astype("int64").copy()
df2.dtypes

df2 = df.copy()
df2["tax"] = df2["Salary"].apply(lambda x : "20%" if x >= 50000 else "10%")

name_map = {"Alice" : "A" , "Bob" : "B"}

df2["Name"] = df2["Name"].map(name_map)

df2.assign(new_salary = df2["Salary"] * 1.1)

df2["Department"].replace("HR", "REcurator")
df2.columns = ["Id", "Name", "Age", "Department", "Salary", "tax"]
df2.rename(columns={"Salary":"Income"})
df2.rename(index={1:"First"})
df2.sort_values("Salary")
# df2.sort_values("Salary", ascending = False)
sorted_df = df2.sort_values(["Salary", "Age"])

sorted_df.sort_index()
#ranking bases

# sorted_df.reset_index()
# sorted_df.reset_index(drop=True)

# sorted_df["Ranking"] = soretd_df["Salary"].rank()
# sorted_df