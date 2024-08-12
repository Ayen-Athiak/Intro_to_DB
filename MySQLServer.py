import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Establish a connection to the MySQL server
        connection = mysql.connector.connect(
            host='localhost', 
            user ='root',
            password ='ayen@12',
          
            database ='alx_book_store'       
        )

        if connection.is_connected():
            cursor = connection.cursor()
            
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")
    
    except Error as e:
      
        print(f"Error: {e}")
    
   

if __name__ == "__main__":
    create_database()
