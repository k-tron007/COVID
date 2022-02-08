import mysql.connector
conn=mysql.connector.connect(host='localhost', user='root', password='miok0909', db='archit')
cursor=conn.cursor()
#Log-in
while True:
    ID=input("Enter id: ")
    password=input("Enter pass: ")
    if(ID=='' and password==''):
        while True:
            Active = int(input("Enter no. of Active cases: "))
            Confirmed = int(input("Enter no. of Confirmed cases: "))
            Recovered = int(input("Enter no. of Recovered cases: "))
            Death = int(input("Enter no. of Deaths: "))
            print(" Active=", Active,
                  "\n Confirmed=", Confirmed,
                  "\n Recovered=", Recovered,
                  "\n Deaths=", Death)
            a= input("Is the above data correct? (Y or N)")
            if(a=='Y'):
                break
            elif(a=='N'):
                pass
            else:
                print("Invalid input!")
                pass
        cursor.execute("insert into COVID values(curdate()," + str(Active) + "," + str(Confirmed) + "," + str(Recovered) + "," + str(Death) + ")")
        conn.commit()
        print("Data saved")
        input("Press Enter to exit")
        break
    else:
        print("Incorrect credentials!")
        pass
