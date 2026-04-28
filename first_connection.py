# Import the library
import mysql.connector as mydbconnection
from mysql.connector import Error

def connect():
    conn = None

    try: 
        # Establish a connection
        conn = mydbconnection.connect(database='classicmodels',user='root', password='password')
        
        
        # Perform SQL Operations
        # Return result (get results from SQL)
        if conn.is_connected():
            print('Connected to MySQL DB')

    except Error  as e:
        print(f'❌ Error: {e}')

    finally: # runs whether operation failed  or not (always run)     
        # Close your connection
        if conn is not None  and conn.is_connected():
            conn.close()
            print('🛑 DB Connection Closed')

# Module if state
if __name__=='__main__':
    connect()