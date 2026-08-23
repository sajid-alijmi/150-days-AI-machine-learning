import pandas as pd

df2 = df.copy()

new_col_order = [col for col in df2.columns if col != "ID"] + ["ID"]
print(new_col_order)
df2[new_col_order]

# df2 = df.copy()

# df2 = df2.drop_duplicate()
# df2 = df2.fillna(0)

# df2 = df2.sort_value("Salary")

# df2 = df2.reset_index(drop=True)
df2.to_csv("sorted_data.csv")

df.groupby("Department")["Salary"].mean()
df.groupby("Department")["Salary"].min()

#df.groupby("gender")["income"].mean()
#df.groupby("gender")["income"].max()

df.groupby("Department")["Salary"].agg(["mean", "min", "max"])
df.groupby("Department")["Salary"].aggregate(["mean", "min", "max"])

df.groupby("Department")["Salary"].agg(avg_salary="mean", min_salary="min",max_salary="max")

df.groupby("Department").agg({
    "Salary" : "mean",
    "Age"  : "mean"
})
df = pd.DataFrame({
    "country": ["USA", "USA", "India", "India"],
    "year": [2020, 2021, 2020, 2021],
    "sales": [100, 120, 90, 110],
    "profit":[20, 25, 18, 22]
})
melted_df = df.melt(
    id_vars = ["country", "year"],
    value_vars = ["sales", "profit"],
    var_name = "metrices",
    value_name = "value"
)
melted_df.pivot(
    index=["country", "year"],
    columns="metrices",
    values = "value"
)

df = pd.read_csv("employer_data.csv")

df["Age"].hist()

df.plot(kind="scatter", x="Age", y="Salary")