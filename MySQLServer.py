import mysql.connector

try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="myusername",
        password="mypassword",
        database="mydatabase"
    )
except mysql.connector.Error as err:
    print(f"Error connecting to the database: {err}")
    exit(1)


mycursor = mydb.cursor()

mycursor.execute(
    "CREATE DATABASE IF NOT EXISTS alx_book_store"
)

if mycursor:
    print("Database created successfully or already exists.")
