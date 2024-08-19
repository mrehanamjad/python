import mysql.connector
from dotenv import load_dotenv
import os
import hashlib

# Load environment variables from .env file
load_dotenv()

# Retrieve environment variables
db_host = os.getenv('DB_HOST')
db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')
db_name = os.getenv('DB_NAME')

# Connect to MySQL
connection = mysql.connector.connect(
    host=db_host,
    user=db_user,
    password=db_password,
    database=db_name
)

cursor = connection.cursor()

def hash_password(password):
    """Hashes a password using SHA-256."""
    return hashlib.sha256(password.encode()).hexdigest()

def sign_up(name, email, password):
    """Registers a new user."""
    hashed_password = hash_password(password)
    try:
        cursor.execute("INSERT INTO users (name, email, password) VALUES (%s, %s, %s)",
                       (name, email, hashed_password))
        connection.commit()
        print("User registered successfully!")
    except mysql.connector.Error as err:
        print(f"Error: {err}")

def login(email, password):
    """Logs in a user."""
    hashed_password = hash_password(password)
    try:
        cursor.execute("SELECT * FROM users WHERE email = %s AND password = %s",
                       (email, hashed_password))
        user = cursor.fetchone()
        if user:
            print(f"Welcome, {user[1]}!")
        else:
            print("Invalid email or password.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")

def main():
    while True:
        choice = input("Do you want to (1) Sign Up or (2) Login? Enter 1 or 2: ")
        if choice == '1':
            name = input("Enter your name: ")
            email = input("Enter your email: ")
            password = input("Enter your password: ")
            sign_up(name, email, password)
        elif choice == '2':
            email = input("Enter your email: ")
            password = input("Enter your password: ")
            login(email, password)
        else:
            print("Invalid choice. Please try again.")
        continue_choice = input("Do you want to continue? (yes/no): ")
        if continue_choice.lower() != 'yes':
            break

if __name__ == "__main__":
    main()

# Close the cursor and the connection when done
cursor.close()
connection.close()
