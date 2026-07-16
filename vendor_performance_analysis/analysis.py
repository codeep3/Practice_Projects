import pandas as pd
from sqlalchemy import create_engine
files=["begin_inventory","end_inventory","purchase_prices","purchases","sales","vendor_invoice"]
og_path=r"C:\Users\nerth\Desktop\CODING\DA_course\Projects\vendor_performance_analysis\data"
engine=create_engine("postgresql://postgres:codex_dbms@localhost:5432/vendor_db")
for i in range(6):
    new_path=og_path + f"\{files[i]}.csv"
    df=pd.read_csv(new_path)
    df.to_sql(files[i],engine,if_exists="replace",index=False)

