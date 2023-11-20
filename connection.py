# create connection
import mysql.connector
con = mysql.connector.connect(host='localhost', user='root', passwd='', database='test')
db = con.cursor()
