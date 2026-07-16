import pandas as pd
from sqlalchemy import create_engine
df = pd.read_csv(r"C:\Users\nerth\Desktop\CODING\DA_course\Projects\Customer_shopping_behaviour_analysis\data set\customer_shopping_behavior.csv")
# cleaning the data
df.columns=df.columns.str.lower()
df.columns=df.columns.str.replace(" ","_")
df=df.rename(columns={"purchase_amount_(usd)":"purchase_amount"})
df["review_rating"]=df.groupby("category")["review_rating"].transform(lambda x:x.fillna(x.median()))

# creating new columns 
#age_group
labels=['Young Adult','Adult','Middle-aged','Senior']
df['age_group']= pd.qcut(df['age'],q=4,labels=labels).astype("str")
#purchase_frequency_days
frequency_mapping={
"Every 3 Months":    90,
"Annually":365,
"Quarterly":90,
"Monthly":30,
"Bi-Weekly":14,
"Fortnightly":14,
"Weekly":7
}
df["purchase_frequency_days"]=df["frequency_of_purchases"].map(frequency_mapping)

#removing "promo_code_used" because it's redundant and we already have the info in "discount_applied"
df=df.drop("promo_code_used",axis=1) 

#connecting with Dbeaver
engine = create_engine("postgresql://postgres:codex_dbms@localhost:5432/csb_db")
df.to_sql("customer_shopping_behavior",engine,if_exists="replace",index=False)
print("Done")