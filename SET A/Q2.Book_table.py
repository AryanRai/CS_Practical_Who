import mysql.connector as mycon
mydb = mycon.connect(host='localhost', user='root', passwd='root', database='library')  #statement 1
mycursor = mydb.cursor() #statement 2
mycursor.execute('select * from book')  #statement 3
row = mycursor.fetchone() #statement 4
print(row)



