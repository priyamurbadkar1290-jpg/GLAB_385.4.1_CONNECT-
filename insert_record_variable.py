# Import libraries
import mysql.connector as mydbconnection
from mysql.connector import Error

def connect(id, name, price, purchase_date):
    conn = None
    
    try:
        # Establish Connection
        conn = mydbconnection.connect(
            database='usersdb',
            user='root',
            password='password'
        )
        print('🎉 Established DB Connection')

        cursor = conn.cursor()

        mySql_insert_query = """INSERT INTO Laptop (Id, Name, Price, Purchase_date)VALUES (%s, %s, %s, %s) """                

        record = (id, name, price, purchase_date) # Putting values in tuple for insertion into query

        # Execute query
        cursor.execute(mySql_insert_query, record)
        conn.commit()
        print('✅ Records successfully added to Laptop table')

        # Collect results

    except Error as e:
        print(f'❌ Error: {e}')
    
    finally:
        # Close Connection
        if conn is not None and conn.is_connected():
            conn.close()
            print('🛑 Connection to SQL Closed')
        
if __name__ == '__main__':
    connect(23, 'MacBook Pro', 5000, '2026-01-01')
    connect(24, 'Chromebook', 500, '202-01-01')
    
        







