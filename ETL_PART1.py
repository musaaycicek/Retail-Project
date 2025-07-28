

import pandas as pd
from Database_conn import conn_db


  
conn=conn_db()

# En çok satan ürünler
   
df_sales=pd.read_sql("SELECT * FROM sales",conn)
satıs=df_sales.groupby("PRODUCT_ID")["QUANTITY"].sum().sort_values(ascending=False).head()

print(satıs)
conn.close()
