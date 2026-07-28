import pandas as pd
import psycopg2
from sqlalchemy import create_engine , text
import os as o
from time import perf_counter

start = perf_counter()


base_url=r"C:\Users\nerth\Desktop\CODING\DA_course\practice_projects\vendor_performance_analysis\data"

engine=create_engine("postgresql://postgres:codex_dbms@localhost:5432/vendor_db")

def create_table(table_name:str,sql_engine,dataframe):
    dataframe.to_sql(table_name,sql_engine,if_exists="replace",index=False)
    print("Table Creation Complete✅")

def empty_table(table_name:str,sql_engine):
    with sql_engine.begin() as conn:
        conn.execute(text("truncate table "+str(table_name)+";"))
    print("Table Data Erased Successfully🗑️")
def copy_table(path:str,sql_engine,table_name:str):
    with sql_engine.raw_connection() as conn:
        with conn.cursor() as cur:
            with open(path,"r",encoding="utf-8") as f:
                cur.copy_expert(
                    "COPY "+table_name+" FROM STDIN WITH CSV HEADER",f
                )
        conn.commit()
    print(f"{table_name} Data Ingestion Complete📝")

files=o.listdir("data")
for i in range(len(files)):
    url=base_url+"\\"+files[i]
    df=pd.read_csv(url,nrows=1000)
    df.columns=df.columns.str.lower()
    df.columns=df.columns.str.replace(" ","_")
    name=files[i].replace(".csv","")
    create_table(table_name=name,sql_engine=engine,dataframe=df)
    empty_table(table_name=name,sql_engine=engine)
    copy_table(table_name=name,sql_engine=engine,path=url)


end = perf_counter()

print(f"Execution time: {end - start:.3f} seconds")
