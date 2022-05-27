import pyodbc 

server = 'AZURE MSSQL SERVER'
database = 'Azure MSSQL' 
username = 'Azure MSSQL User' 
password = 'Azure MSSQL Password' 

#Conecction String
driver='DRIVER={ODBC Driver 17 for SQL Server};'
others=f"SERVER={server};DATABASE={database};UID={username};PWD={password}"
connection_string='{}{}'.format(driver,others)

con = pyodbc.connect(connection_string)

cur = con.cursor()
res=cur.execute("SELECT @@VERSION AS 'SQL Server Version Details'")
for r in res:
    print(r[0])