df=pd.read_csv("Covid19.csv")
cov = pd.DataFrame(df, columns=["DATE","ACTIVE",
"RECOVERED","CONFIRMED","DEATHS"])
ch='y'
while ch=='y' or ch=='Y':
                print("\nMain Menu")
                print("\n1.Fetch Data")
                print("2.Dataframe Statistics")
                print("3.Display Records")
                # print("4.Search specific row/column")
                print("4.Data Visualization")
                print("5.Data analytics")
                print("6.Exit")
                
                ch1=input("\nEnter your choice")
                
                if ch1==str(1):
                    print("\n DISPLAYING DAILY SPIKES IN COVID CASES IN THE MONTH OF AUG AND SEP 2020")
                    print("=============================")
                    print(cov.to_string(index=False))
                    input("\nPress Enter to go back")
                    pass
                
                elif ch1==str(2):
                    while(True):
                        print("\nDataframe Statistics Menu")
                        print("1.Display all column names")
                        print("2.Display the indexes")
                        print("3.Display the shape")
                        print("4.Display the dimension")
                        print("5.Display the data types of all columns")
                        print("6.Display the size")
                        print("7.Exit")
                        
                        ch2=input("\nEnterchoice")
                        
                        if ch2==str(1):
                            print(cov.columns)
                            input("\nPress Enter to go back")
                            pass
                        
                        elif ch2==str(2):
                            print(cov.index)
                            input("\nPress Enter to go back")
                            pass
                        
                        elif ch2==str(3):
                            print(cov.shape)
                            input("\nPress Enter to go back")
                            pass
                        
                        elif ch2==str(4):
                            print(cov.ndim)
                            input("\nPress Enter to go back")
                            pass
                        
                        elif ch2==str(5):
                            print(cov.dtypes)
                            input("\nPress Enter to go back")
                            pass
                        
                        elif ch2==str(6):
                            print(cov.size)
                            input("\nPress Enter to go back")
                            pass
                        
                        elif ch2==str(7):    
                            break
                        
                elif ch1==str(3):
                    while(True):
                        print("\nDisplay Records Menu")
                        print("\n1.Top 5 Resords")
                        print("2.Bottom 5 Records")
                        print("3.Specific number of records from the top")
                        print("4.Specific number of records from the bottom")
                        # print("5.Display records of a specific date")
                        # print("6.Display records of all dates")
                        print("5.Exit")

                        ch3=input("\nEnterchoice")

                        if ch3==str(1):
                            print(cov.head())
                            input("\nPress Enter to go back")
                            pass

                        elif ch3==str(2):
                            print(cov.tail())
                            input("\nPress Enter to go back")
                            pass

                        elif ch3==str(3):
                            n=int(input("\nEnter how many records you want to display from the top"))
                            print(cov.head(n))
                            input("\nPress Enter to go back")
                            pass

                        elif ch3==str(4):
                            n=int(input("\nEnter how many records you want to display from the bottom"))
                            print(cov.tail(n))
                            input("\nPress Enter to go back")
                            pass

                        elif ch3 == str(5):
                            break

                elif ch1==str(4):
                    while(True):
                        print("\nData Visualization Menu")
                        print("\n1.Line Plot--> No. of active cases")
                        print("2.Histogram--> No. of recovered ")
                        print("3.Horizontal Bar Plot--> No. of confirmed cases")
                        print("4.Vertical bar plot-->No.of deaths")
                        print("5.Exit")

                        ch5=input("\nEnter choice")

                        if ch5==str(1):
                            x = cov['DATE']
                            y = cov['ACTIVE']
                            plt.plot(x,y)
                            plt.title("No.of active cases")
                            plt.xlabel("DATE")
                            plt.ylabel("ACTIVE CASES")
                            plt.show()
                            
                        elif ch5==str(2):
                            plt.hist([cov.DATE,cov.RECOVERED],bins=100,edgecolor="black",color=['orange','red'])
                            plt.title("No.of recovered")
                            plt.xlabel("DATE")
                            plt.ylabel("RECOVERED")
                            plt.show()
                            
                        elif ch5==str(3):
                            plt.barh(cov.DATE,cov.CONFIRMED)
                            plt.title("No. of confirmed cases")
                            plt.xlabel("DATE")
                            plt.ylabel("CONFIRMED CASES")
                            plt.show()
                            
                        elif ch5==str(4):
                            plt.bar(cov.DATE,cov.DEATHS)
                            plt.title("No.of deaths")
                            plt.xlabel("DATE")
                            plt.ylabel("DEATHS")
                            plt.show()
                            
                        elif ch5==str(5):
                            break
                        
                elif ch1==str(5):
                    while(True):
                        print("\nData Analytics Menu")
                        print("\n1.Date on which maximum active cases were observed")
                        print("2.Date on which minimum active cases were observed")
                        print("3.Date on which maximum recovered cases were observed")
                        print("4.Date on which minimum recovered cases were observed")
                        print("5.Date on which maximum confirmed cases were observed")
                        print("6.Date on which minimum confirmed cases were observed")
                        print("7.Date on which maximum deaths were observed")
                        print("8.Date on which minimum deaths were observed")
                        print("9.Exit")

                        ch6=input("\nEnterchoice:")

                        if ch6==str(1):
                            m=cov['ACTIVE'].max()
                            s=cov.loc[cov.ACTIVE==m]
                            print("Date on which maximum active cases were observed--",m,"is\n",s.index)
                            input("\nPress Enter to go back")
                            pass

                        elif ch6==str(2):
                            m=cov['ACTIVE'].min()
                            s=cov.loc[cov.ACTIVE==m]
                            print("Date on which minimum active cases were observed--",m,"is\n",s.index)
                            input("\nPress Enter to go back")
                            pass

                        elif ch6==str(3):
                            m=cov['RECOVERED'].max()
                            s=cov.loc[cov.RECOVERED==m]
                            print("Date on which maximum recovered cases were observed-",m,"is\n",s.index)
                            input("\nPress Enter to go back")
                            pass

                        elif ch6==str(4):
                            m=cov['RECOVERED'].min()
                            s=cov.loc[cov.RECOVERED==m]
                            print("Date on which minimum recovered cases were observed-",m,"is\n",s.index)
                            input("\nPress Enter to go back")
                            pass

                        elif ch6==str(5):
                            m=cov['CONFIRMED'].max()
                            s=cov.loc[cov.CONFIRMED==m]
                            print("Date on which maximum confirmed cases were observed-",m,"is\n",s.index)
                            input("\nPress Enter to go back")
                            pass

                        elif ch6==str(6):
                            m=cov['CONFIRMED'].min()
                            s=cov.loc[cov.CONFIRMED==m]
                            print("Date on which minimum confirmed cases were observed-",m,"is\n",s.index)
                            input("\nPress Enter to go back")
                            pass

                        elif ch6==str(7):
                            m=cov['DEATHS'].max()
                            s=cov.loc[cov.DEATHS==m]
                            print("Date on which maximum deaths were observed-",m,"is\n",s.index)
                            input("\nPress Enter to go back")
                            pass

                        elif ch6==str(8):
                            m=cov['DEATHS'].min()
                            s=cov.loc[cov.DEATHS==m]
                            print("Date on which minimum deaths were observed-",m,"is\n",s.index)
                            input("\nPress Enter to go back")
                            pass

                        elif ch6==str(9):
                            break
                        
                elif ch1==str(6):
                    break
