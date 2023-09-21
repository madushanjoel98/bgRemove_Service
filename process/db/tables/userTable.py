import db.dbConnection as dbc


class UserTable:

    def __init__(self):
        self.my_connection = dbc.MYConnection().get_connection()
        self.create_table()

    def create_table(self):
        cursor = self.my_connection.cursor()
        # Create the table.
        cursor.execute(
            'CREATE TABLE IF NOT EXISTS student.myusers (id INT NOT NULL AUTO_INCREMENT, username VARCHAR(255) NOT NULL, password VARCHAR(255) NOT NULL, PRIMARY KEY (id))')
        cursor.close()
        self.my_connection.close()

    def userLogin(self, username, password):
        self.my_connection._open_connection()
        validtion = bool(False)
        cursor = self.my_connection.cursor()
        cursor.execute(
            'SELECT 1 FROM myusers WHERE username=%s AND password=%s', (username, password))
        if cursor.fetchone():
            validtion = True
        else:
            validtion = False
        cursor.close()
        self.my_connection.close()
        return validtion
