import csv
import MySQLdb

mydb = MySQLdb.connect(host='localhost',
    user='root',
    passwd='neo&trinity',
    db='phone_reviews')
cursor = mydb.cursor()

fileName = raw_input("Enter csv file name: ")

csv_data = csv.reader(file(fileName))

for row in csv_data:
    cursor.execute('INSERT INTO product_list(imageUrl, description, link, name,manufacturer)''VALUES(%s,%s,%s,%s,"Samsung")', row)
#close the connection to the database.

mydb.commit()

cursor.close()
print ("Done")
