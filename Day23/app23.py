import requests

json_data = res.json()

import pandas as pd 

df = pd.json_normalize(json_data["data"])
df = df[['id', 'Title', 'Year', 'ISBN']]

df