
import pymysql
import csv
import pandas as pd

data = pd.read_csv(r'countrys.csv',encoding='utf-8')
df = pd.DataFrame(data)
#crear objeto de la conexion
con = pymysql.connect(host="localhost",port=3306,user="luisdb",passwd="1234",db="paises")
cursor = con.cursor()
for row in df.itertuples():
    sql = "INSERT INTO country (Nombre, poblacion) VALUES (%s,%s)"
    val = (row.Nombre,row.poblacion)
    cursor.execute(sql,val)
    #print(row.Nombre,row.poblacion)
    #print(type(row.Autor))
con.commit() #se guardan los datos
con.close()	