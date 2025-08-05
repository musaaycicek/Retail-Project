import pandas as pd
from Database_conn import conn_db
import seaborn as sns
import matplotlib.pyplot as plt


conn=conn_db()

sql_query=("SELECT PRODUCT_ID,COUNT(QUANTITY) as count_pr FROM SALES GROUP BY PRODUCT_ID "
"ORDER BY count_pr DESC")

df_customer=pd.read_sql(sql_query,conn)


#print(df_customer)

sns.barplot(df_customer)
plt.show()

