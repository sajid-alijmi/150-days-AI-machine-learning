import pandas as pd
import zipfile
import os

# ZIP file ka exact path
zip_path = os.path.join(os.path.dirname(__file__), "archive.zip")

# ZIP extract
with zipfile.ZipFile(zip_path, "r") as zip_ref:
    zip_ref.extractall("dataset")

# Dataset ke andar files check
print(os.listdir("dataset"))

# CSV read
df = pd.read_csv("dataset/GlobalWeatherRepository.csv")

# First 5 rows
print(df.head())

# Particular row
print(df.loc[77])

df.describe()
df.nunique()
df = pd.read_csv("dataset/GlobalWeatherRepository.csv")
# df.head()
# df.describe()
#df[["country", "sunrise]] 
# df.loc[77]
df.iloc[2]
df.columns

df [ df["wind_degree"]>100 ]
#Filtering of data

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