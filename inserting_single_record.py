# Import libraries
import mysql.connector as mydbconnection
from mysql.connector import Error

def connect():
    conn = None

    try:
        # Establish connection
        conn = mydbconnection.connect(
            database='usersdb',
            user='root',
            password='password'
        )
        print('🎉 Connected to SQL DB')

        # Perform SQL Action
        cursor = conn.cursor()

        # Create query
        mySql_insert_query = """INSERT INTO laptop (Id, Name, Price, Purchase_date) 
                           VALUES (23, 'Alienware', 5000, '2017-08-13')"""
        
        # Execute query
        cursor.execute(mySql_insert_query)

        # Commit changes to DB
        conn.commit()
        print(cursor.rowcount, "✅ Record inserted successfully into Laptop Table")

        cursor.close()

    except Error as e:
        print(f'❌ Error: {e}')

    finally:
        # Close Connection
        if conn is not None and conn.is_connected():
            conn.close()
            print('🛑 Db connection closed')


if __name__ == '__main__':
    connect()