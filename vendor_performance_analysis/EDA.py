import pandas as pd
import matplotlib.pyplot as plt
import os
import Data_ingestion as dg

files=os.listdir("data")
path=os.path.abspath("data")
url=path+"\\"+files[5]
file=url.split("\\")[-1]
clean_path=os.path.abspath(r"data\cleaned")
clean_url=clean_path+"\\"+file
print(f"Working On {file}")
print(f"Storing At {clean_url}")
df=pd.read_csv(url)
df.columns=df.columns.str.replace(" ","")
df.columns=df.columns.str.lower()
pd.set_option("display.max_columns",None)
pd.set_option("display.max_rows",None)
#!cleaning and performing EDA 
#?begin_inventory
# df["startDate"]=pd.to_datetime(df["startDate"])
# df.columns=df.columns.str.lower()
# df.columns=df.columns.str.replace(" ","_")
# df["pack"]=df["size"].apply(lambda x : str(x.split(" ")[1]) if "Pk" in x else 0)
# df["size"]=df["size"].apply(lambda x : str(x.split(" ")[0]) if "Pk" in x else x)
# df["size"]=df["size"].replace(r"(?<=\d)mL","",regex=True)
# mask1=df["size"]=="3/100"
# df.loc[mask1,"pack"]=3
# df.loc[mask1,"size"]="100"
# df.drop(df[df["size"]=="Liter"].index,inplace=True)
# df["size"]=df["size"].apply(lambda x: str(float(x.replace("Oz","")) * 29.5735) if "Oz" in str(x) else x)
# df["size"]=df["size"].apply(lambda x: int(float(x.replace("L","")) * 1000) if "L" in str(x) else x)
# mask2=df["size"]=="750 + 2/"
# mask3=df["size"]=="750 + 3/"
# mask4=df["size"]=="750 + 4/"
# df.loc[mask2,"size"]="850"
# df.loc[mask3,"size"]="900"
# df.loc[mask4,"size"]="950"
# df=df.rename(columns={"inventoryid":"inventory_id","onhand":"on_hand","startdate":"start_date"})
# df["size"]=pd.to_numeric(df["size"],errors="raise")
# df.to_csv(clean_url,index=False)
# print(df.info())
# dg.empty_table(table_name="begin_inventory")
# dg.create_table(table_name="begin_inventory",dataframe=df)
# dg.copy_table(table_name="begin_inventory",path=clean_url)

#? end_inventory
# df["endDate"]=pd.to_datetime(df["endDate"])
# df.columns=df.columns.str.lower()
# df.columns=df.columns.str.replace(" ","_")
# df["size"]=df["size"].replace(r"(?<=\d)mL","",regex=True)
# df["size"]=df["size"].replace("Liter",None)
# df["size"]=df["size"].apply(lambda x: float(x.replace("Oz",""))*29.5735 if "Oz" in str(x) else x)
# df.drop(df[df["size"]=="25.0"].index,inplace=True)
# df.dropna(axis=0,inplace=True)
# mask=df["size"]=="3/100"
# mask1=df["size"]=="750 + 1/"
# mask2=df["size"]=="750 + 2/"
# mask3=df["size"]=="750 + 3/"
# mask4=df["size"]=="750 + 4/"
# df.loc[mask,"pack"]=3
# df.loc[mask,"size"]=100
# df.loc[mask1,"size"]="800"
# df.loc[mask2,"size"]="850"
# df.loc[mask3,"size"]="900"
# df.loc[mask4,"size"]="950"
# df["size"]=df["size"].apply(lambda x: float(x.replace("Gal",""))*3785.41 if "Gal" in str(x) else x)
# df["pack"]=df["size"].apply(lambda x: str(x.split(" ")[1]) if "Pk" in str(x) else 0)
# df["size"]=df["size"].apply(lambda x: str(x.split(" ")[0]) if "Pk" in str(x) else x)
# df["size"]=df["size"].apply(lambda x: float(x.replace("L",""))*1000 if "L" in str(x) else x)
# df["size"]=df["size"].apply(lambda x: x.replace(" oz","") if "oz" in str(x) else x)
# df["size"]=df["size"].apply(lambda x: 29.5735*(int(x.split("/")[0])/int(x.split("/")[1])) if "/" in str(x) else x)
# df["size"]=pd.to_numeric(df["size"],errors="raise")
# df.rename(columns={"inventoryid":"inventory_id","enddate":"end_date","onhand":"on_hand"},inplace=True)
# df["pack"]=pd.to_numeric(df["pack"])
# print(df.info())
# df.to_csv(clean_url,index=False)
# dg.create_table(table_name="end_inventory",dataframe=df,only_schema=True)
# dg.copy_table(table_name="end_inventory",path=clean_url)

#?purchase_prices
# df.columns=df.columns.str.lower()
# df.columns=df.columns.str.replace(" ","_")
# df["pack"]=df["size"].apply(lambda x: x.split(" ")[1] if "Pk" in str(x) else 0)
# df["size"]=df["size"].apply(lambda x: x.split(" ")[0] if "Pk" in str(x) else x)
# df.drop(df[df["size"]=="25.0"].index,inplace=True)
# df.drop(df[df["size"]=="Liter"].index,inplace=True)
# df["size"]=df["size"].replace(r"(?<=\d)mL","",regex=True)
# mask=df["size"]=="3/100"
# df.loc[mask,"pack"]=3
# df.loc[mask,"size"]="100"
# df["size"]=df["size"].apply(lambda x: float(x.replace("L",""))*1000 if "L" in str(x) else x)
# df["size"]=df["size"].apply(lambda x: float(x.replace("Oz",""))*29.5735 if "Oz" in str(x) else x)
# df["size"]=df["size"].apply(lambda x: float(x.replace("Gal",""))*3785.41 if "Gal" in str(x) else x)
# df["size"]=df["size"].apply(lambda x: int(x.replace("oz","").split("/")[0])/int(x.replace("oz","").split("/")[1])*3785.41 if "oz" in str(x) else x)
# mask1=df["size"]=="750 + 1/"
# mask2=df["size"]=="750 + 2/"
# mask3=df["size"]=="750 + 3/"
# df.loc[mask1,"size"]="800"
# df.loc[mask2,"size"]="850"
# df.loc[mask3,"size"]="900"
# df["pack"]=pd.to_numeric(df["pack"])
# df["size"]=pd.to_numeric(df["size"],errors="raise")
# df=df.rename(columns={"inventoryid":"inventory_id","vendornumber":"vendor_number","vendorname":"vendor_name","podate":"po_date","ponumber":"po_number","receivingdate":"receiving_date","invoicedate":"invoice_date",
# "paydate":"pay_date","purchaseprice":"purchase_price"})
# df.to_csv(clean_url,index=False)
# df[["podate","invoicedate","paydate","receivingdate"]]=df[["podate","invoicedate","paydate","receivingdate"]].apply(pd.to_datetime)
# dg.create_table(table_name="purchases",dataframe=df,only_schema=True)
# dg.copy_table(table_name="purchases",path=clean_url)

#? code to delete every table inside database
# for file in files:
#     if file == "cleaned":
#         continue
#     else :
#         x=file.replace(".csv","")
#         dg.del_table(table_name=x)

#?purchase_prices
# df.columns=df.columns.str.replace(" ","")
# df.columns=df.columns.str.lower()
# print(df["size"].value_counts())
# print(df[df["size"]=="750mL 12 P"],"This")
# df["pack"]=df["size"].apply(lambda x: x.split(" ")[1] if "P" in str(x) else 0)
# df["size"]=df["size"].apply(lambda x: x.split(" ")[0] if "P" in str(x) else x)
# mask1=df["size"]=="750mL + 1/"
# mask2=df["size"]=="750mL + 3/"
# mask3=df["size"]=="750mL + 4/"
# mask4=df["size"]=="750mL  3"
# df.loc[mask1,"size"]="800"
# df.loc[mask2,"size"]="900"
# df.loc[mask3,"size"]="950"
# df.loc[mask4,"size"]="900"
# df.drop(df[df["size"]=="Unknown"].index,inplace=True)
# df["size"]=df["size"].apply(lambda x: x.replace("mL","") if "mL" in str(x) else x)
# df["size"]=df["size"].apply(lambda x: x.replace("ml","") if "ml" in str(x) else x)
# df[["size","volume"]]=df[["size","volume"]].apply(pd.to_numeric)
# df=df.rename(columns={"purchaseprice":"purchase_price","vendornumber":"vendor_number","vendorname":"vendor_name"})
# df.to_csv(clean_url,index=False)
# dg.create_table(table_name="purchase_prices",dataframe=df,only_schema=True)
# dg.copy_table(table_name="purchase_prices",path=clean_url)


#?vendor_invoice
# pd.set_option("display.max_rows",None)
# df.rename(columns={"vendornumber":"vendor_number","vendorname":"vendor_name","invoicedate":"invoice_date","ponumber":"po_number","podate":"po_date","paydate":"pay_date"},inplace=True)
# df.to_csv(clean_url,index=False)
# dg.create_table(table_name="vendor_invoice",dataframe=df,only_schema=True)
# dg.copy_table(table_name="vendor_invoice",path=clean_url)

#?sales
df.drop(df[df["size"]=="25.0"].index,inplace=True)
df.drop(df[df["size"]=="Liter"].index,inplace=True)
df.drop(df[df["size"]=="25"].index,inplace=True)
df["pack"]=df["size"].apply(lambda x: x.split(" ")[1] if "Pk" in str(x) else 0)
df["size"]=df["size"].apply(lambda x: x.split(" ")[0] if "Pk" in str(x) else x)
df["size"]=df["size"].replace(r"(?<=\d)mL","",regex=True)
df["size"]=df["size"].apply(lambda x: float(x.replace("L",""))*1000 if "L" in str(x) else x)
df["size"]=df["size"].apply(lambda x: float(x.replace("Oz",""))*29.5735 if "Oz" in str(x) else x)
# df["size"]=df["size"].apply(lambda x: float(x.replace("Gal",""))*3785.41 if "Gal" in str(x) else x)
df["size"]=df["size"].apply(lambda x: int(x.replace("oz","").split("/")[0])/int(x.replace("oz","").split("/")[1])*3785.41 if "oz" in str(x) else x)
mask1=df["size"]=="750 + 1/"
mask2=df["size"]=="750 + 2/"
mask3=df["size"]=="750 + 3/"
mask4=df["size"]=="750 + 4/"
df.loc[mask1,"size"]="800"
df.loc[mask2,"size"]="850"
df.loc[mask3,"size"]="900"
df.loc[mask4,"size"]="950"
mask=df["size"]=="3/100"
df.loc[mask,"pack"]=3
df.loc[mask,"size"]="100"
df["pack"]=pd.to_numeric(df["pack"])
df["size"]=pd.to_numeric(df["size"],errors="raise")
df.rename(columns={"inventoryid":"inventory_id","salesquantity":"sales_quantity","salesdollars":"sales_dollars","salesprice":"sales_price","salesdate":"sales_date","excisetax":"excise_tax","vendorno":"vendor_no","vendorname":"vendor_name"},inplace=True)
df.to_csv(clean_url,index=False)
dg.create_table(table_name="sales",dataframe=df,only_schema=True)
dg.copy_table(table_name="sales",path=clean_url)

