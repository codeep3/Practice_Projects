import pandas as pd
import psycopg2
from sqlalchemy import create_engine , text
import os as o
from time import perf_counter

def time(func):
    def wrapper(*args,**kwargs):
        start = perf_counter()
        func(*args,**kwargs)
        end = perf_counter()
        print(f"Execution time: {end - start:.3f} seconds")
    return wrapper
base_url=r"C:\Users\nerth\Desktop\CODING\DA_course\practice_projects\vendor_performance_analysis\data"

engine=create_engine("postgresql://postgres:codex_dbms@localhost:5432/vendor_db")

@time
def empty_table(table_name:str,sql_engine=engine):
    with sql_engine.begin() as conn:
        conn.execute(text("truncate table "+str(table_name)+";"))
    print("Table Data Erased Successfully🗑️")

@time
def create_table(table_name:str,dataframe,sql_engine=engine,only_schema:bool=False):
    dataframe.head(1000).to_sql(table_name,sql_engine,if_exists="replace",index=False)
    if only_schema:
        empty_table(table_name=table_name)
    print("Table Creation Complete✅")

@time
def copy_table(path:str,table_name:str,sql_engine=engine):
    with sql_engine.raw_connection() as conn:
        with conn.cursor() as cur:
            with open(path,"r",encoding="utf-8") as f:
                cur.copy_expert(
                    "COPY "+ table_name +" FROM STDIN WITH CSV HEADER",f
                )
        conn.commit()
    print(f"{table_name} Data Ingestion Complete📝")

def del_table(table_name:str,sql_engine=engine):
    with sql_engine.raw_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(f"DROP TABLE IF EXISTS {table_name}")
        conn.commit()
    print(f"{table_name} Deleted !❌!")

