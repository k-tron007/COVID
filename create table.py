import mysql.connector
conn=mysql.connector.connect(host='localhost', user='root', password='miok0909', db='archit')
cursor=conn.cursor()
cursor.execute("create table COVID (Date date, Active int, Confirmed int, Recovered int, Death int)")
conn.commit()
