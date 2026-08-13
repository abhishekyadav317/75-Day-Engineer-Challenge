# database.py establish a SQLite caonnection and initialize the database schema 

import sqlite3

def get_connection():
    connection = sqlite3.connect("expenses.db")
    return connection



def initialize_database():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS expenses(
        id INTEGER PRIMARY KEY ,
        amount REAL ,
        category TEXT ,
        description TEXT ,
        date TEXT
        );





    ''')

    connection.commit()
    connection.close()

initialize_database()    

'''

        INSERT INTO expenses (amount , category , description , date )
        values
            (250, 'Food', 'Lunch', '2026-08-10'),
            (500, 'Travel', 'Bus ticket', '2026-08-10'),
            (120.50, 'Food', 'Breakfast', '2026-08-10');
            (800 , 'Shopping' , 'Shoes' , '2026-08-11' )
            (150, 'Food', 'Dinner', '2026-08-11');

'''
