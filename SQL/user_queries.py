import mysql.connector
from mysql.connector import Error
from User.profile import Person
import sqlalchemy
from sqlalchemy import create_engine, Column, Integer, String, JSON
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


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

cursor = connection.cursor()


engine = create_engine("mysql+mysqlconnector://kai:hack_24@localhost/userdata")

# Define the base class
Base = sqlalchemy.orm.declarative_base()

# Define the User table model
class User(Base):
    __tablename__ = 'user_list'

    hashed_password = Column(String(255), primary_key=True)
    username = Column(String(20))
    total_revenue = Column(Integer)
    total_profit = Column(Integer)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Close the session
session.close()


def user_to_SQL(user:Person):
    query = "INSERT INTO user_list (username, hashed_password, total_revenue, total_profit) VALUES (%s, %s, %s, %s)"
    values = (user.username, user.password, 0, 0)

    cursor.execute(query, values)
    connection.commit()

    print(f"{cursor.rowcount} row(s) inserted.")

def update_revenue_and_profit(user:Person):
    query = "UPDATE user_list SET total_revenue = %s WHERE hashed_password = %s VALUES(%s,%s)"
    values = (user.total_revenue,user.password)
    query2 = "UPDATE user_list SET total_profit = %s WHERE hashed_password = %s VALUES(%s,%s)"
    values2 = (user.total_profit,user.password)

    cursor.execute(query, values)
    cursor.execute(query2, values2)
    connection.commit()

    print(f"{cursor.rowcount} row(s) inserted.")

def update_password(user:Person,old_password:str):
    query = "UPDATE user_list SET hashed_password = %s WHERE hashed_password = %s VALUES(%s,%s)"
    values = (user.password,old_password)

    cursor.execute(query, values)
    connection.commit()

    print(f"{cursor.rowcount} row(s) inserted.")

def update_username(user:Person):
    query = "UPDATE user_list SET username = %s WHERE hashed_password = %s VALUES(%s,%s)"
    values = (user.username,user.password)

    cursor.execute(query, values)
    connection.commit()

    print(f"{cursor.rowcount} row(s) inserted.")

def SQL_to_user(user:Person,user_username:str):
    template = session.query(User).filter_by(username = user_username).first()
    user.username = template.username
    user.password = template.hashed_password
    user.total_revenue = template.total_revenue
    user.total_profit = template.total_profit














