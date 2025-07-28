

import pandas as pd
from Database_conn import conn_db

conn=conn_db()

# En çok alışveriş yapan müşteri

df_customers = pd.read_sql("SELECT * FROM CUSTOMERS", conn)
df_sales = pd.read_sql("SELECT * FROM SALES", conn)

customer_sales=df_sales.groupby("CUSTOMER_ID")["QUANTITY"].sum()
top_customer_id = customer_sales.idxmax()



print("En çok alışveriş yapan müşteri ID:", top_customer_id)
# En çok müşteri hangisi ise onun verilerini getir
print(df_customers[df_customers["CUSTOMER_ID"] == top_customer_id])
