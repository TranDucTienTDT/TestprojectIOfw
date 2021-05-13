import mysql.connector

mydb = mysql.connector.connect(
  host="db",
  user="root",
  password="12345"
)

print(mydb)