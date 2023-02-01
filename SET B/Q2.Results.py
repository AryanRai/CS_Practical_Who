import mysql.connector as mycon
mydb = mycon.connect(host='localhost', user='root', passwd='root', database='school') #statement 1
mycursor = mydb.cursor() #statement 2
mycursor.execute("UPDATE result SET Marks = 90 WHERE Reg_No = 10923") #statement 3
mydb.commit() #statement 4
print(mycursor.rowcount,"record(s) affected")

