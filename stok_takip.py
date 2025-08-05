
import pandas as  pd
import matplotlib.pyplot as plt
import seaborn as sn
from Database_conn import conn_db


query=("SELECT s.sale_id,s.sale_date,ı.product_id, ı.current_stock-(Select Sum(quantity)as miktar from sales"
       " WHERE product_id = i.product_id GROUP BY product_ıd) as Mevcut"
       " FROM sales s JOIN ınventory ı On s.product_id=ı.product_id"
       )

   

conn=conn_db()

sql_query=(query)
cnn=pd.read_sql(sql_query,conn)
print(cnn)

conn.close()

