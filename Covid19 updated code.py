import pandas as pd

import matplotlib.pyplot as plt

df=pd.read_excel("C:\\Users\\archi\\Documents\\Covid19.xlsx",index_col=0)

cov = pd.DataFrame(df, columns=["ACTIVE",
"RECOVERED","CONFIRMED","DEATHS"])
               
ch='y'
               
while ch=='y' or ch=='Y':

                print("Main Menu")
               
                print("1.Fetch Data")
               
                print("2.Dataframe Statistics")
               
                print("3.Display Records")
               
                # print("4.Search specific row/column")
               
                print("4.Data Visualization")
               
                print("5.Data analytics")
               
               
                print("6.Exit")
               
                ch1=int(input("Enter your choice"))


                if ch1==1:
                    print(" DISPLAYING DAILY SPIKES IN COVID CASES IN THE MONTH OF AUG AND SEP 2020")
                    print("=============================")
                    print(cov)
                elif ch1==2:
                    while(True):
                        print("Dataframe Statistics Menu")
                       
                        print("1.Display all column names")
                       
                        print("2.Display the indexes")
                       
                        print("3.Display the shape")
                       
                        print("4.Display the dimension")
                       
                        print("5.Display the data types of all columns")
                       
                        print("6.Display the size")
                       
                        print("7.Exit")
                       
                        ch2=int(input("Enterchoice"))
                        if ch2==1:
                    
                            print(cov.columns)
                    
       
                        elif ch2==2:
                    
                            print(cov.index)
                    
                        elif ch2==3:
                    
                            print(cov.shape)
                    
                        elif ch2==4:
                    
                            print(cov.ndim)
                    
                        elif ch2==5:

                            print(cov.dtypes)
                    
                        elif ch2==6:

                            print(cov.size)

                        elif ch2==7:    
                    
                            break
                
                elif ch1==3:
                    
                    while(True):
                        
                        print("Display Records Menu")

                        print("1.Top 5 Resords")

                        print("2.Bottom 5 Records")


                        print("3.Specific number of records from the top")

                        print("4.Specific number of records from the bottom")

                        # print("5.Display records of a specific date")

                        # print("6.Display records of all dates")

                        print("5.Exit")
                        
                        ch3=int(input("Enterchoice"))
                        
                        if ch3==1:

                            print(cov.head())
                            
                        elif ch3==2:

                            print(cov.tail())
                            
    

                       
                        elif ch3==3:

                            n=int(input("Enter how many records you want to display from the top"))

                            print(cov.head(n))

                        elif ch3==4:

                            n=int(input("Enter how many records you want to display from the bottom"))

                            print(cov.tail(n))
                            
                            
                        elif ch3 == 5:

                            break

                elif ch1==4:
                    while(True):

                        print("Data Visualization Menu")

                        print("1.Line Plot--> No. of active cases")

                        print("2.Histogram--> No. of recovered ")

                        print("3.Horizontal Bar Plot--> No. of confirmed cases")

                        print("4.Vertical bar plot-->No.of deaths")

                        print("5.Exit")


                        ch5=int(input("Enter choice"))

                        if ch5==1:

                            x = cov.index

                            y = cov['ACTIVE']

                            plt.plot(x,y)

                            plt.title("No.of active cases")

                            plt.xlabel("DATE")

                            plt.ylabel("ACTIVE CASES")

                            plt.show()
                            
                        elif ch5==2:

                            plt.hist([cov.index,cov.RECOVERED],bins=100,edgecolor="black",color=['orange','red'])

                            plt.title("No.of recovered")

                            plt.xlabel("DATE")

                            plt.ylabel("RECOVERED")

                            plt.show()
                            
                        elif ch5==3:

                            plt.barh(cov.index,cov.CONFIRMED)

                            plt.title("No. of confirmed cases")

                            plt.xlabel("DATE")

                            plt.ylabel("CONFIRMED CASES")

                            plt.show()

                        elif ch5==4:

                            plt.bar(cov.index,cov.DEATHS)

                            plt.title("No.of deaths")

                            plt.xlabel("DATE")

                            plt.ylabel("DEATHS")

                            plt.show()

                        elif ch5==5:

                            break

                elif ch1==5:

                    while(True):

                        print("Data Analytics Menu")

                        print("1.Date on which maximum active cases were observed")


                        print("2.Date on which minimum active cases were observed")

                        print("3.Date on which maximum recovered cases were observed")

                        print("4.Date on which minimum recovered cases were observed")

                        print("5.Date on which maximum confirmed cases were observed")

                        print("6.Date on which minimum confirmed cases were observed")

                        print("7.Date on which maximum deaths were observed")

                        print("8.Date on which minimum deaths were observed")

                        print("9.Exit")

                        ch6=int(input("Enterchoice:"))

                        if ch6==1:

                            m=cov['ACTIVE'].max()

                            s=cov.loc[cov.ACTIVE==m]

                            print("Date on which maximum active cases were observed--",m,"is\n",s.index)
                            

                        elif ch6==2:

                            m=cov['ACTIVE'].min()

                            s=cov.loc[cov.ACTIVE==m]
                            print("Date on which minimum active cases were observed--",m,"is\n",s.index)

           
                        elif ch6==3:

                            m=cov['RECOVERED'].max()

                            s=cov.loc[cov.RECOVERED==m]


                            print("Date on which maximum recovered cases were observed-",m,"is\n",s.index)


                        elif ch6==4:

                            m=cov['RECOVERED'].min()

                            s=cov.loc[cov.RECOVERED==m]

                            print("Date on which minimum recovered cases were observed-",m,"is\n",s.index)


                        elif ch6==5:

                            m=cov['CONFIRMED'].max()

                            s=cov.loc[cov.CONFIRMED==m]

                            print("Date on which maximum confirmed cases were observed-",m,"is\n",s.index)

                        elif ch6==6:

                            m=cov['CONFIRMED'].min()

                            s=cov.loc[cov.CONFIRMED==m]

                            print("Date on which minimum confirmed cases were observed-",m,"is\n",s.index)

                        elif ch6==7:

                            m=cov['DEATHS'].max()


                            s=cov.loc[cov.DEATHS==m]

                            print("Date on which maximum deaths were observed-",m,"is\n",s.index)

                        elif ch6==8:

                            m=cov['DEATHS'].min()

                            s=cov.loc[cov.DEATHS==m]


                            print("Date on which minimum deaths were observed-",m,"is\n",s.index)

                        elif ch6==9:

                            break

                elif ch1==6:
                    pass
