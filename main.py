import pandas as pd
import matplotlib.pyplot as plt
import mysql.connector
conn=mysql.connector.connect(host='localhost', user='root', password='miok0909', db='archit')
cursor=conn.cursor()

while True:
    print("\nMAIN MENU")
    print("\n1. Data Manipulation")
    print("2. Data Retrieval and Analysis")
    print("3. Quit")
    mm=input("\nEnter your choice: ")

    if mm==str(1):
        exec(open('UI.py').read())
        pass
    elif mm==str(2):
        exec(open('Admin thingy.py').read())
        pass
    elif mm==str(3):
        print("Quitting...")
        break
    else:
        print("\nInvalid input")
        pass
