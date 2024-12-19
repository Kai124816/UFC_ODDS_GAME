import bcrypt 
import mysql.connector
from mysql.connector import Error

# Replace these with your local database details
HOST = "localhost"
USER = "kai"
PASSWORD = "hack_24"
DATABASE = "userdata"

try:
    # Establish the connection
    connection = mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        database=DATABASE
    )

    if connection.is_connected():
        print("Connected to MySQL database")

except Error as e:
    print(f"Error: {e}")

finally:
    # Close the connection if it was established
    if 'connection' in locals() and connection.is_connected():
        connection.close()
        print("Connection closed.")

