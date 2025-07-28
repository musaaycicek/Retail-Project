
import oracledb

def conn_db():
 conn = oracledb.connect(
   user="sys",
    password="sifre123",
    dsn="localhost:1521/ORCLPDB1",
    mode=oracledb.SYSDBA  

 )
 return conn
     


    
  


