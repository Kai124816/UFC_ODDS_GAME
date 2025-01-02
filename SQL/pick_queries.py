from User.profile import Person
from User.predictions import Picks
from Fight_Card.card_constructor import Card
from Fight_Card.fight import Fight
import mysql.connector
from mysql.connector import Error
import sqlalchemy
from sqlalchemy import cast
from sqlalchemy.types import Date
from sqlalchemy import create_engine, Column, Integer, String, JSON
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import MetaData
from sqlalchemy import Table
from sqlalchemy import select
import datetime

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
        query = f"""
        CREATE TABLE `{table_name}` (
            Card DATE,
            Fighter VARCHAR(50),
            Method VARCHAR(10),
            Outcome VARCHAR(10),
            Amount_Placed INT
        );
        """

        cursor.execute(query)

        # Close the connection
        cursor.close()
        connection.close()

    except mysql.connector.Error as e:
        print(f"Error: {e}")

def store_picks(user: Person):
    try:
        connection = create_connection()

        # Create a cursor object
        cursor = connection.cursor()

        picks = user.picks.picks
        card = user.picks.card
        table_name = user.username + "_picks "

        # Parameterized query for safety
        query = "INSERT INTO " + table_name + "(Card, Fighter, Method, Outcome, Amount_Placed) VALUES (%s, %s, %s, %s, %s)"

        if table_exists(table_name):
            for pick in picks:
                values = (card.date, pick[0], pick[1], pick[2], pick[3])
                cursor.execute(query, values)
        else:
            create_table(user)
            for pick in picks:
                values = (card.date, pick[0], pick[1], pick[2], pick[3])
                cursor.execute(query, values)

        # Commit the transaction
        connection.commit()

        print("Picks stored successfully.")

        # Close the connection
        cursor.close()
        connection.close()

    except mysql.connector.Error as e:
        print(f"Error: {e}")

def SQL_to_Picks(user: Person, date: datetime.date):
    # Create database engine
    engine = create_engine("mysql+mysqlconnector://kai:hack_24@localhost/userdata")
    connection = engine.connect()
    metadata = MetaData()

    # Reflect the table
    table_name = user.username + "_picks"
    table = Table(table_name, metadata, autoload_with=engine)

    # Create a query
    query = select(table).where(table.c["Card"] == date)

    # Execute the query and fetch results
    result = connection.execute(query)
    rows = result.fetchall()

    # Close the connection
    connection.close()

    for row in rows:
        pick = []
        pick.append(row[1])
        pick.append(row[2])
        pick.append(row[3])
        pick.append(row[4])
        user.picks.picks.append(pick)

def delete_user(user: Person):
    """
    Deletes a user's table and associated data from the database.

    :param user: An instance of the Person class, representing the user.
    """
    try:
        connection = create_connection()

        # Create a cursor object
        cursor = connection.cursor()

        # Define the table name
        table_name = f"{user.username}_picks"

        # Check if the table exists
        if table_exists(table_name):
            # Drop the table
            cursor.execute(f"DROP TABLE {table_name};")
            print(f"Table '{table_name}' successfully deleted.")
        else:
            print(f"Table '{table_name}' does not exist.")

        # Close the connection
        cursor.close()
        connection.close()

    except mysql.connector.Error as e:
        print(f"Error: {e}")








