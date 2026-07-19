import pandas as pd
from sqlalchemy import create_engine
df=pd.read_csv(r"C:\Users\nerth\Desktop\CODING\DA_course\practice_projects\Health_analysis\data\ocd_patient_dataset.csv")
# converting into snake casing
df.columns=df.columns.str.lower()
df.columns=df.columns.str.replace(" ","_")

#uploading to SQL 
engine=create_engine("postgresql://postgres:codex_dbms@localhost:5432/health_db")
df.to_sql("ocd",engine,if_exists="replace",index=False)
print("data uploaded to server")