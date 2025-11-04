#Read .csv file in series

import pandas as pd

df = pd.read_csv("data.csv")

s = df["Names"]

print(s)