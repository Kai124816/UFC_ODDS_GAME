from User.profile import Person
from User.predictions import Picks
from Fight_Card.card_constructor import Card
from Fight_Card.fight import Fight
import mysql.connector
from mysql.connector import Error
import sqlalchemy
from sqlalchemy import create_engine, Column, Integer, String, JSON
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

def create_connection():
    connection = None
    try:
        connection = mysql.connector.connect(
            host='localhost',         # Your MySQL server host
            user='kai',     # Your MySQL username
            password='hack_24',  # Your MySQL password
            database='userdata' # The database you want to access)
        )

        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection

def create_session():
    engine = create_engine("mysql+mysqlconnector://kai:hack_24@localhost/userdata")

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()
    return session

def table_exists(table_name: str):
    """
    Check if a table exists in a specific MySQL database.

    :param table_name: Name of the table to look for.
    :param password: MySQL password (default is an empty string).
    :return: True if the table exists, False otherwise.
    """
    try:
        connection = create_connection()

        # Create a cursor object
        cursor = connection.cursor()

        # Query to check for table existence
        
        cursor.execute(f"SHOW TABLES LIKE '{table_name}';")
        result = cursor.fetchone()

        # Close the connection
        cursor.close()
        connection.close()

        # Return True if the table exists, False otherwise
        return result is not None

    except mysql.connector.Error as e:
        print(f"Error: {e}")
        return False
    
def create_table(user:Person):
    table_name = f"{user.username}_picks"
    try:
        connection = create_connection()

        # Create a cursor object
        cursor = connection.cursor()

        # Query to check for table existence
        
        cursor.execute(f"CREATE TABLE {table_name} (
                        Card DATE,
                        Fighter varchar(50),
                        Method varchar(10),
                        Outcome varchar(10),
                        Amount_Placed INT
                        );")

        # Close the connection
        cursor.close()
        connection.close()

    except mysql.connector.Error as e:
        print(f"Error: {e}")

def store_pick(user:Person,pick:list,card:Card):
    try:
        connection = create_connection()

        # Create a cursor object
        cursor = connection.cursor()

        # Query to check for table existence
        query = f"""
        INSERT INTO {user.username}_picks (Card, Fighter, Method, Outcome, Amount_Placed)
        VALUES ('{card.date}', '{pick[0]}', '{pick[1]}', '{pick[2]}', {pick[3]});
        """
        if table_exists(table_name="{user.username}_picks"):
            cursor.execute(query)
        else:
            create_table(user)
            cursor.execute(query)

        # Close the connection
        cursor.close()
        connection.close()

    except mysql.connector.Error as e:
        print(f"Error: {e}")







