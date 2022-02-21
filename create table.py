import mysql.connector
conn=mysql.connector.connect(host='localhost', user='root', password='miok0909', db='archit')
cursor=conn.cursor()
cursor.execute("create table COVID (Date date, Active int, Confirmed int, Recovered int, Death int)")
cursor.execute("create table deleted_data (Date date, Active int, Confirmed int, Recovered int, Death int, Deleted_on date)")
cursor.execute("create table altered_data (Date date, iAct int, fAct int, iCon int, fCon int, iRec int ,fRec int, iDet int, fDet int, Altered_on date)")
conn.commit()
