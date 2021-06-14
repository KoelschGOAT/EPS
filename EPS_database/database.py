import sqlite3


class DatabaseInterface:
    def __init__(self):
        self.connection = sqlite3.connect("User.db")
        self.cursor = self.connection.cursor()

    def execute(self, query, data):
        self.cursor.execute(query, data)
        self.connection.commit()
        return self.cursor

    def execute_table(self, query):
        self.cursor.execute(query)
        self.connection.commit()
        return self.cursor

    def create_table(self):
        return """CREATE TABLE IF NOT EXISTS Accounts(Personal_Number TEXT PRIMARY KEY NOT NULL, PIN TEXT, Balance Decimal(6,2))"""

    def change_balance(self, ban, balance):
        """ Assigns a league_id to a user which is a foreign key """
        return self.execute("UPDATE Accounts SET Balance = ? WHERE ban = ?", (balance, ban))

    def add_user_to_account(self, ban, pin, balance):
        """ This function is only called  during initial set up of game, populates the player db with players. """
        return self.execute("INSERT INTO Accounts (Personal_Number, PIN, Balance) VALUES(?, ?, ?)", (ban, pin, balance))

    def __del__(self):
        """ Destroys instance and connection on completion of called method """
        self.connection.close()
