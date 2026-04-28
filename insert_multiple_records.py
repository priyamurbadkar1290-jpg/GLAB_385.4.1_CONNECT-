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
        print('🎉 Succesfull Connection to SQL DB')

        # Query and values
        mySql_insert_query = """INSERT INTO Laptop (Id, Name, Price, Purchase_date)
        VALUES (%s, %s, %s, %s) """

        records_to_insert = [
            (4, 'HP Pavilion Power', 1999, '2019-01-11'),
            (5, 'MSI WS75 9TL-496', 5799, '2019-02-27'),
            (6, 'Microsoft Surface', 2330, '2019-07-23')
        ]

        # Excute Query
        cursor = conn.cursor()

        cursor.executemany(mySql_insert_query, records_to_insert)
        conn.commit()
        print(f'✅ {cursor.rowcount}: Records inserted successfully')
        
    except Error as e:
        print(f'❌ Error: {e}')
    
    finally:
        # Close connections
        if conn is not None and conn.is_connected():
            conn.close()
            print('🛑 SQL DB connection closed')
            


if __name__ == '__main__':
    connect()