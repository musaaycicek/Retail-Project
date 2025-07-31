
import pandas as pd
from Database_conn import conn_db

conn=conn_db()

veri=pd.read_sql("SELECT * FROM CUSTOMERS",conn)

pivotdata=veri.pivot_table(values="CUSTOMER_ID",index="NAME",columns="CITY")

print(pivotdata)
print()

# En çok müşterisi olan şehirler
print(pivotdata.sum(axis=0))

# Bir müşteri birden fazla şehirde bulunursa

musteri_sehirler=pivotdata[pivotdata.gt(0).sum(axis=1)>1] 
print(musteri_sehirler)


