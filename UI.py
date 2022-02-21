while True:
    print("\nDATA MANIPULATION MENU")
    print("\n1. Enter today's data")
    print("2. Alter today's data(if wrong data is entered by mistake)")
    print("3. Enter data of custom date")
    print("4. Alter data of specific date")
    print("5. Delete data of specific date")
    print("6. Exit")
    ch= input("\nEnter your choice: ")
    if ch==str(1):
        while True:
            password=input("\nEnter passcode: ")
            if password=='':
                Active = int(input("\nEnter no. of Active cases: "))
                Confirmed = int(input("Enter no. of Confirmed cases: "))
                Recovered = int(input("Enter no. of Recovered cases: "))
                Death = int(input("Enter no. of Deaths: "))
                cursor.execute("insert into COVID values(curdate()," + str(Active) + "," + str(Confirmed) + "," + str(Recovered) + "," + str(Death) + ")")
                conn.commit()
                cursor.execute("select * from COVID")
                data=cursor.fetchall()
                df=pd.DataFrame(data, columns=["DATE","ACTIVE","RECOVERED","CONFIRMED","DEATHS"])
                q=df.to_csv('Covid19.csv')
                print("\nData saved")
                input("Press Enter to exit")
                break
            else:
                print("\nIncorrect credentials!")
                pass
    elif ch==str(2):
        while True:
            password=input("\nEnter passcode: ")
            if password=='':
                cursor.execute("select * from covid where Date=curdate()")
                a=cursor.fetchall()
                b=pd.DataFrame(a, columns=["DATE","ACTIVE","RECOVERED","CONFIRMED","DEATHS"])
                iact=b["ACTIVE"].to_string(index=False)
                icon=b["CONFIRMED"].to_string(index=False)
                irec=b["RECOVERED"].to_string(index=False)
                idet=b["DEATHS"].to_string(index=False)
                Active = int(input("\nEnter no. of Active cases: "))
                Confirmed = int(input("Enter no. of Confirmed cases: "))
                Recovered = int(input("Enter no. of Recovered cases: "))
                Death = int(input("Enter no. of Deaths: "))
                cursor.execute("update covid set Active="+str(Active)+", Confirmed="+str(Confirmed)+", Recovered="+str(Recovered)+", Death="+str(Death)+" where Date=curdate()")
                cursor.execute("insert into altered_data values(curdate(),"+str(iact)+","+str(Active)+","+str(icon)+","+str(Confirmed)+","+str(irec)+","+str(Recovered)+","+str(idet)+","+str(Death)+",curdate())")
                conn.commit()
                cursor.execute("select * from COVID")
                data=cursor.fetchall()
                df=pd.DataFrame(data, columns=["DATE","ACTIVE","RECOVERED","CONFIRMED","DEATHS"])
                q=df.to_csv('Covid19.csv')
                cursor.execute("select * from altered_data")
                dd=cursor.fetchall()
                ddf=pd.DataFrame(dd, columns=["DATE","I-ACTIVE","F-ACTIVE","I-RECOVERED","F-RECOVERED","I-CONFIRMED","F-CONFIRMED","I-DEATHS","F-DEATHS","ALTERED ON"])
                ddc=ddf.to_csv('Restricted\\Altered_data.csv')
                print("\nData saved")
                input("Press Enter to exit")
                break
            else:
                print("\nIncorrect credentials!")
                pass
    elif ch==str(3):
        while True:
            password=input("\nEnter passcode: ")
            if password=='':
                Date=input("\nEnter date in yyyy/mm/dd format: ")
                Active = int(input("Enter no. of Active cases: "))
                Confirmed = int(input("Enter no. of Confirmed cases: "))
                Recovered = int(input("Enter no. of Recovered cases: "))
                Death = int(input("Enter no. of Deaths: "))
                cursor.execute("insert into COVID values('"+str(Date)+"'," + str(Active) + "," + str(Confirmed) + "," + str(Recovered) + "," + str(Death) + ")")
                conn.commit()
                cursor.execute("select * from COVID")
                data=cursor.fetchall()
                df=pd.DataFrame(data, columns=["DATE","ACTIVE","RECOVERED","CONFIRMED","DEATHS"])
                q=df.to_csv('Covid19.csv')
                print("\nData saved")
                input("Press Enter to exit")
                break
            else:
                print("\nIncorrect credentials!")
                pass
    elif ch==str(4):
        while True:
            password=input("\nEnter passcode: ")
            if password=='':
                Date=input("\nEnter date in yyyy/mm/dd format: ")
                cursor.execute("select * from covid where Date='"+str(Date)+"'")
                a=cursor.fetchall()
                b=pd.DataFrame(a, columns=["DATE","ACTIVE","RECOVERED","CONFIRMED","DEATHS"])
                iact=b["ACTIVE"].to_string(index=False)
                icon=b["CONFIRMED"].to_string(index=False)
                irec=b["RECOVERED"].to_string(index=False)
                idet=b["DEATHS"].to_string(index=False)
                Active = int(input("Enter no. of Active cases: "))
                Confirmed = int(input("Enter no. of Confirmed cases: "))
                Recovered = int(input("Enter no. of Recovered cases: "))
                Death = int(input("Enter no. of Deaths: "))
                cursor.execute("update covid set Active="+str(Active)+", Confirmed="+str(Confirmed)+", Recovered="+str(Recovered)+", Death="+str(Death)+" where Date='"+str(Date)+"'")
                cursor.execute("insert into altered_data values('"+str(Date)+"',"+str(iact)+","+str(Active)+","+str(icon)+","+str(Confirmed)+","+str(irec)+","+str(Recovered)+","+str(idet)+","+str(Death)+",curdate())")
                conn.commit()
                cursor.execute("select * from COVID")
                data=cursor.fetchall()
                df=pd.DataFrame(data, columns=["DATE","ACTIVE","RECOVERED","CONFIRMED","DEATHS"])
                q=df.to_csv('Covid19.csv')
                cursor.execute("select * from altered_data")
                dd=cursor.fetchall()
                ddf=pd.DataFrame(dd, columns=["DATE","I-ACTIVE","F-ACTIVE","I-RECOVERED","F-RECOVERED","I-CONFIRMED","F-CONFIRMED","I-DEATHS","F-DEATHS","ALTERED ON"])
                ddc=ddf.to_csv('Restricted\\Altered_data.csv')
                print("\nData saved")
                input("Press Enter to exit")
                break
            else:
                print("\nIncorrect credentials!")
                pass
    elif ch==str(5):
        while True:
            password=input("\nEnter the passcode: ")
            if password=='':
                Date=input("\nEnter date in yyyy/mm/dd format: ")
                cursor.execute("select * from covid where Date='"+str(Date)+"'")
                a=cursor.fetchall()
                b=pd.DataFrame(a, columns=["DATE","ACTIVE","RECOVERED","CONFIRMED","DEATHS"])
                iact=b["ACTIVE"].to_string(index=False)
                icon=b["CONFIRMED"].to_string(index=False)
                irec=b["RECOVERED"].to_string(index=False)
                idet=b["DEATHS"].to_string(index=False)
                cursor.execute("insert into deleted_data values('"+str(Date)+"',"+str(iact)+","+str(icon)+","+str(irec)+","+str(idet)+",curdate())")
                cursor.execute("delete from covid where Date='"+str(Date)+"'")
                conn.commit()
                cursor.execute("select * from covid")
                data=cursor.fetchall()
                df=pd.DataFrame(data, columns=["DATE","ACTIVE","RECOVERED","CONFIRMED","DEATHS"])
                q=df.to_csv('Covid19.csv')
                cursor.execute("select * from deleted_data")
                dd=cursor.fetchall()
                ddf=pd.DataFrame(dd, columns=["DATE","ACTIVE","RECOVERED","CONFIRMED","DEATHS","DELETED ON"])
                ddc=ddf.to_csv('Restricted\\Deleted_data.csv')
                print("\nData updated")
                print("Press Enter to exit")
                break
            else:
                print("\nIncorrect credentials!")
                pass
    elif ch==str(6):
        print("\nExitting...")
        break
