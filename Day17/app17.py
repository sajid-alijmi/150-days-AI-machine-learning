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