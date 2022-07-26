import sqlite3
from datetime import datetime
from time import strftime
from os import remove, system

# Connect to databace
conn = sqlite3.connect("spend_lists.db")

# Cursor
Cursor = conn.cursor()

def init() : 
    "Create Table"

    Cursor.execute('''CREATE TABLE IF NOT EXISTS spend ( 
        amount INTEGER ,
        category TEXT COLLATE NOCASE ,
        message TEXT , 
        date TEXT  
        )''')




def add(amount , category , msg = None) : 

    now = datetime.now()
    with conn : 
        Cursor.execute("INSERT INTO spend VALUES (:amount , :category , :message , :date)" , 
        {'amount' : amount , 'category' : category , 'message' : msg , 'date' : now.strftime('%Y - %m - %d | %H:%M')})
        conn.commit()


    print("Spend Inserted ! ")


def show(category = None): 
    """Show item in the databae ! """

    if category == None : 
        Cursor.execute('''SELECT * FROM spend''')
        Result = (Cursor.fetchall())

        Cursor.execute('''SELECT amount FROM spend''')
        Result2 = (Cursor.fetchall())
        
        total = 0
        for i in Result2 : 
            total += i[0]


        return Result , total


    elif category != None : 
        Cursor.execute('''SELECT * FROM spend WHERE category = :category ''' , {'category' : category})
        Result = Cursor.fetchall()

        Cursor.execute('''SELECT amount FROM spend WHERE category = :category''' , {'category' : category})
        Result2 = (Cursor.fetchall())
        
        sum_not_none = 0
        for i in Result2 : 
            sum_not_none += i[0]

        return Result , sum_not_none


def Delete(category = None) : 
    if category == None : 
        input("Enter any thing for delete all spneds , are you sure ?")

        conn.close()
        remove('spend_lists.db')

        print("data bace removed :( ")

    elif category != None : 
        input(f"Enter any thing for delete spneds of category : {category} , are you sure ?")

        Cursor.execute("DELETE FROM spend WHERE category = :category" , 
        {'category' : category})

        conn.commit()
        conn.close()
    

