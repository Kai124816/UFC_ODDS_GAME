import mysql.connector
from mysql.connector import Error
from User.profile import Person
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

def user_to_SQL(user: Person):
    """
    Inserts a new user's information into the 'user_list' table in the database.

    Args:
        user (Person): The user object containing username and hashed password.

    Returns:
        None

    Raises:
        Exception: If an error occurs during the database query or connection.
    """
    try:
        connection = create_connection()
        cursor = connection.cursor()
        rowcount1 = cursor.rowcount

        query = "INSERT INTO user_list (username, hashed_password, total_revenue, total_profit) VALUES (%s, %s, %s, %s)"
        values = (user.username, user.password, 0, 0)

        cursor.execute(query, values)
        connection.commit()

        print(f"{cursor.rowcount - rowcount1} row(s) inserted.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        cursor.close()
        connection.close()


def update_revenue_and_profit(user: Person):
    """
    Updates the total revenue and profit for a specific user in the 'user_list' table.

    Args:
        user (Person): The user object containing updated revenue and profit values.

    Returns:
        None

    Raises:
        Exception: If an error occurs during the database query or connection.
    """
    try:
        # Establish the connection
        connection = create_connection()
        cursor = connection.cursor()

        # Single query to update both columns
        query = """
        UPDATE user_list 
        SET total_revenue = %s, total_profit = %s 
        WHERE hashed_password = %s;
        """
        values = (user.total_revenue, user.total_profit, user.password)

        # Execute the query
        cursor.execute(query, values)

        # Commit changes to the database
        connection.commit()

        print(f"1 row updated.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Close the cursor and connection
        cursor.close()
        connection.close()


def update_password(user: Person, old_password: str):
    """
    Updates a user's password in the 'user_list' table.

    Args:
        user (Person): The user object with the new password.
        old_password (str): The current password to be updated.

    Returns:
        None

    Raises:
        Exception: If an error occurs during the database query or connection.
    """
    try:
        connection = create_connection()
        cursor = connection.cursor()

        query = "UPDATE user_list SET hashed_password = %s WHERE hashed_password = %s;"
        values = (user.password, old_password)

        cursor.execute(query, values)
        connection.commit()

        print(f"1 row updated.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        cursor.close()
        connection.close()


def update_username(user: Person):
    """
    Updates a user's username in the 'user_list' table.

    Args:
        user (Person): The user object with the new username.

    Returns:
        None

    Raises:
        Exception: If an error occurs during the database query or connection.
    """
    try:
        connection = create_connection()
        cursor = connection.cursor()

        query = "UPDATE user_list SET username = %s WHERE hashed_password = %s;"
        values = (user.username, user.password)

        cursor.execute(query, values)
        connection.commit()

        print(f"1 row updated.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        cursor.close()
        connection.close()


def SQL_to_user(user: Person, user_username: str):
    """
    Retrieves a user's data from the database and updates the user's object with that information.

    Args:
        user (Person): The user object to be updated with data from the database.
        user_username (str): The username of the user whose data is to be fetched.

    Returns:
        None

    Raises:
        sqlalchemy.exc.SQLAlchemyError: If an error occurs during the database query or connection.
    """
    session = create_session()

    # Define the base class
    Base = sqlalchemy.orm.declarative_base()
    # Define the User table model
    class User(Base):
        __tablename__ = 'user_list'

        hashed_password = Column(String(255), primary_key=True)
        username = Column(String(20))
        total_revenue = Column(Integer)
        total_profit = Column(Integer)

    template = session.query(User).filter_by(username=user_username).first()
    user.username = template.username
    user.password = template.hashed_password
    user.total_revenue = template.total_revenue
    user.total_profit = template.total_profit
    session.close()


def delete_user(username: str):
    """
    Deletes a user from the 'user_list' table based on the username.

    Args:
        username (str): The username of the user to be deleted.

    Returns:
        None

    Raises:
        Exception: If an error occurs during the database query or connection.
    """
    try:
        connection = create_connection()
        cursor = connection.cursor()
        rowcount1 = cursor.rowcount

        query = "DELETE FROM user_list WHERE username = %s;"
        values = (username,)

        cursor.execute(query, values)
        connection.commit()

        print(f"{rowcount1 - cursor.rowcount} row(s) deleted.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        cursor.close()
        connection.close()
