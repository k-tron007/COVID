while True:
    print("\nDATA MANIPULATION MENU")
    print("\n1. Enter today's data")
    print("2. Alter today's data(if wrong data is entered by mistake)")
    print("3. Enter data of custom date")
    print("4. Alter data of specific date")
    print("5. Exit")
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
                #cursor.execute("select * from COVID where Date=curdate()")
                cursor.execute("select * from COVID")
                data=cursor.fetchall()
                df=pd.DataFrame(data, columns=["DATE","ACTIVE","RECOVERED","CONFIRMED","DEATHS"])
                #a=pd.read_csv('Covid19.csv',index_col=0)
                #dtf=pd.DataFrame(a, columns=["DATE","ACTIVE","RECOVERED","CONFIRMED","DEATHS"])
                #b=dtf.append(df, ignore_index=True)
                #q=b.to_csv('Covid19.csv')
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
                Active = int(input("\nEnter no. of Active cases: "))
                Confirmed = int(input("Enter no. of Confirmed cases: "))
                Recovered = int(input("Enter no. of Recovered cases: "))
                Death = int(input("Enter no. of Deaths: "))
                cursor.execute("update covid set Active="+str(Active)+", Confirmed="+str(Confirmed)+", Recovered="+str(Recovered)+", Death="+str(Death)+" where Date=curdate()")
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
                #cursor.execute("select * from COVID where Date='"+str(Date)+"'")
                cursor.execute("select * from COVID")
                data=cursor.fetchall()
                df=pd.DataFrame(data, columns=["DATE","ACTIVE","RECOVERED","CONFIRMED","DEATHS"])
                #a=pd.read_csv('Covid19.csv',index_col=0)
                #dtf=pd.DataFrame(a, columns=["DATE","ACTIVE","RECOVERED","CONFIRMED","DEATHS"])
                #b=dtf.append(df, ignore_index=True)
                #q=b.to_csv('Covid19.csv')
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
                Active = int(input("Enter no. of Active cases: "))
                Confirmed = int(input("Enter no. of Confirmed cases: "))
                Recovered = int(input("Enter no. of Recovered cases: "))
                Death = int(input("Enter no. of Deaths: "))
                cursor.execute("update covid set Active="+str(Active)+", Confirmed="+str(Confirmed)+", Recovered="+str(Recovered)+", Death="+str(Death)+" where Date='"+str(Date)+"'")
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
    elif ch==str(5):
        print("\nExitting...")
        break
