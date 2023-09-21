import mysql.connector as mysql


class MYConnection:
    def __init__(self):
        self.mydb = mysql.connect(
            host="localhost",
            user="root",
            password="12345",
            database="student"  # Replace with the name of your database
        )

    def get_connection(self):
        if self.mydb.is_connected():
            print("Connected to MySQL database")
            return self.mydb
        else: 
            raise Exception("Connection Failed Please reconnect")


# Create an instance of the Connection class
mysqlconnection = MYConnection().get_connection()
# Check if the connection was successful