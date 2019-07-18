import pyodbc

from util.constant import *

cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+usernamemcas+';PWD='+ password)

cursor = cnxn.cursor()

cursor.execute("SELECT @@version;")
row = cursor.fetchone()
while row:
        print(row[0])
        row = cursor.fetchone()
# print(row)