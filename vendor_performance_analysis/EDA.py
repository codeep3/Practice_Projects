import pandas as pd
import matplotlib.pyplot as plt
import os
import Data_ingestion as dg
#cleaning and performing EDA on begin_inventory
files=os.listdir("data")
path=os.path.abspath("data")
url=path+"\\"+files[0]
df=pd.read_csv(url)
pd.set_option("display.max_columns",None)
df["startDate"]=pd.to_datetime(df["startDate"])
df.columns=df.columns.str.lower()
df.columns=df.columns.str.replace(" ","_")

print(df["size"].value_counts())
