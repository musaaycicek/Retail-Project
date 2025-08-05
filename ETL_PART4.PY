
import pandas as pd
from Database_conn import conn_db

conn=conn_db()

df=pd.read_sql("SELECT * FROM SALES",conn)

df['gün']=df['SALE_DATE'].dt.day_name()
print(df['gün'])

avg_sale=df.groupby('gün')['QUANTITY'].mean().sort_values(ascending=False)

print(avg_sale)
