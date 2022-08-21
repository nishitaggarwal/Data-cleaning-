import pandas as pd
import csv 

df = pd.read_csv("final.csv")
print(df.shape)

del df["Luminosity"]

df.to_csv("Final_checked.csv")