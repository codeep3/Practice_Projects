import psycopg2
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

conn = psycopg2.connect(
    database="bda_db",
    user="postgres",
    host="localhost",
    password="codex_dbms",
    port=5432
    )


query='''
    SELECT * FROM banking_clients
'''

df=pd.read_sql(query,con=conn)

#! segmentation
    #! estimated income
bin1=[0,100000,300000,float('inf')]
Label1=["Low","Medium","High"]

df["income_range"]=pd.cut(df["estimated_income"],bins=bin1,labels=Label1)
    #! age 
bin2=[0,20,50,max(df["age"])]
Label2=["Teen","Adult","Senior_Citizen"]
df["age_group"]=pd.cut(df["age"],bins=bin2,labels=Label2)


#! categorical columns 
    #* Univariate analysis

# print(df.info())
cols=[  'nationality', 'fee_structure',
       'loyalty_classification', 'income_range','age_group',
       'amount_of_credit_cards', 'bank_loans',
        'properties_owned',
       'risk_weighting', 'brid', 'genderid', 'iaid']
# for col in df[cols]:
    # sns.countplot(df[col])
    # input("next?")

for i,predictor in enumerate(df[['nationality', 'fee_structure',
       'loyalty_classification', 'income_range','age_group',
       'amount_of_credit_cards', 'bank_loans',
        'properties_owned',
       'risk_weighting', 'brid', 'genderid', 'iaid']]):
    plt.figure(i)
    sns.countplot(data=df,x=predictor)
    plt.show()
    input("Next??")


###! Going Forwad I'll Be Using ipynb File For Analysis 
###! It Is Easier To Write Code And Get Output On Same Window