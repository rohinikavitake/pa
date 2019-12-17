import mysql.connector
mydb = mysql.connector.connect(host="localhost",username="root",password="root")
mycursor = mydb.cursor()
mycursor.exeute('show database')
for i in mycursor:
     print(i)


