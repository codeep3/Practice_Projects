import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
import plotly.colors as colors

pio.templates.default="plotly_white"
df=pd.read_csv(r"C:\Users\nerth\Desktop\CODING\DA_course\Projects\E_commerce_analysis\data\Sample - Superstore.csv",encoding="latin1")
#!converting data types

df["Order Date"] = pd.to_datetime(df["Order Date"])#* pd.to_datetime changes datatype pf the specified column.
df["Ship Date"] = pd.to_datetime(df["Ship Date"])

#!creating new columns

df["Order Month"]=df["Order Date"].dt.month
df["Order Year"]=df["Order Date"].dt.year#* .dt.month/year etc extracts specific date-time data from a value
df["Order Day Of Week"]=df["Order Date"].dt.day_of_week

#1converting headers into snake casing
df.columns=df.columns.str.lower()
df.columns=df.columns.str.replace(" ","_")

#!creating month_name column
name_mapping={
    1:"Jan",
    2:"Feb",
    3:"Mar",
    4:"Apr",
    5:"May",
    6:"Jun",
    7:"Jul",
    8:"Aug",
    9:"Sept",
    10:"Oct",
    11:"Nov",
    12:"Dec"
}
df["order_month_name"]=df["order_month"].map(name_mapping)

#!monthly sales review
sales_by_month=df.groupby("order_month_name")["sales"].sum().reset_index()
#* reset_index gives the newly made series an index , and it help prevent column not found error while plotting a graph.
#* if we do not reset the index , the uses the first column(eg:order_month_name) as index and not as a column hence later giving order_month_name not found error.
    #!plot line graph
# fig=px.line(sales_by_month,#? data frame/series
#            x="order_month_name",#? x axis value
#            y="sales",#? y axis value
#            title="Monthly Sales",#? category_orders allows us to customize the order of any axis
#            category_orders={"order_month_name":[ "Jan", "Feb", "Mar", "Apr", "May", "Jun",
#                                                 "Jul", "Aug", "Sept", "Oct", "Nov", "Dec"]})
            
# fig.show()

#! monthly profit analysis
profit_by_month=df.groupby("order_month_name")["profit"].sum().reset_index()
    #! plotting the data

# fig=px.line( data_frame=profit_by_month,
#             x="order_month_name",
#             y="profit",
#             title="Monthly Profit Analyis",
#             color_discrete_sequence=px.colors.colorbrewer.Reds_r,
#             hover_data={"profit":":.2f"},#? helps modify the tolltips on the figure
#             )
# fig.show()



#!sales by category

sales_by_category= df.groupby("category")["sales"].sum().reset_index()
    #!plotting pie chart
# fig=px.pie(sales_by_category,
#            values="sales",
#            names="category",
#            title="Sales By Category",
#            hole=0.35,
#            color_discrete_sequence=px.colors.carto.Armyrose_r
#            #color_discrete_sequence allows us to choose from 100+ colors paletes
# )
# fig.update_traces(textposition='inside',textinfo='percent + label') 
# #* customize the displayed information on figure. 
# fig.update_layout(title_text='Sales Analysis By Category',title_font=dict(size=50))
# #* .update_layout updates the title text and it's font
# #* title_font only accepts dict values and size can toggle the title size up and down
# fig.show()

#! sales analysis by sub category
# sales_by_sub_category= df.groupby("sub-category")["sales"].sum().reset_index()
# fig=px.bar(data_frame=sales_by_sub_category,
#            x="sub-category",
#            y="sales"
#            )
# fig.show()

#! profit analysis by category and sub-category
#!category
# profit_by_category=df.groupby("category")["sales"].sum().reset_index()
    #! graph
# fig=px.bar(data_frame=profit_by_category,
#            x="category",
#            y="sales",
#            title="Profit By Category",
#            hover_data={"sales":":.2f"}
# )
# fig.show()

#!sub-category
# profit_by_sub_category=df.groupby("sub-category")["sales"].sum().reset_index()
    #! graph
# fig=px.bar(data_frame=profit_by_sub_category,
#            x="sub-category",
#            y="sales",
#            title="Profit By Sub Category",
#            hover_data={"sales":":.2f"}
# )
# fig.show()

#! analysis of sales and profit by customer segment
#! profit
profit_by_customer_segment=df.groupby("segment")["profit"].sum().reset_index()
    #! graph
# fig=px.bar(
#     data_frame=profit_by_customer_segment,
#     x="segment",
#     y="profit",
#     title="Profit By Customer Segment"
# )
# fig.show()
#! sales
sales_by_customer_segment=df.groupby("segment")["sales"].sum().reset_index()
    #! graph
# fig=px.bar(
#     data_frame=sales_by_customer_segment,
#     x="segment",
#     y="sales",
#     title="Sales By Customer Segment"
# )
# fig.show()

#! analysis of sales and profit by segment
sales_proft_by_segment=df.groupby("segment").agg({"sales":"sum","profit":"sum"}).reset_index()
# fig=go.Figure()
#     #! plotting sales bar
# fig.add_trace(go.Bar(x=sales_proft_by_segment['segment'],
#         y=sales_proft_by_segment['sales'],
#         name="Sales",
#         marker_color=colors.carto.Oryel_r
# ))
#     #! plotting profit bar
# fig.add_trace(go.Bar(
#     x=sales_proft_by_segment["segment"],
#     y=sales_proft_by_segment["profit"],
#     name="Profit",
#     marker_color=colors.carto.Redor
# ))
# fig.update_layout(title="sales & profit comparison by segment".capitalize(),xaxis_title="Customer Segment",yaxis_title="Amount")
# fig.show()

#! sales to profit ratio 
sales_proft_by_segment["sales_to_profit_ratio"]=sales_proft_by_segment["sales"]/sales_proft_by_segment["profit"]
print(sales_proft_by_segment[['segment','sales_to_profit_ratio']])