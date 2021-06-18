import sqlite3


class DatabaseInterface:
    def __init__(self):
        self.connection = sqlite3.connect("User.db")
        self.cursor = self.connection.cursor()

    def execute(self, query, data):
        self.cursor.execute(query, data)
        self.connection.commit()
        return self.cursor

    def execute_without(self, query):
        self.cursor.execute(query)
        self.connection.commit()
        return self.cursor

    def create_table(self):     
        return self.execute_without("CREATE TABLE IF NOT EXISTS Accounts(id INTEGER PRIMARY KEY AUTOINCREMENT, number Text, pin TEXT, balance Decimal(6,2))")


    def change_balance(self, num, balance):
        """ Assigns a league_id to a user which is a foreign key """
        return self.execute("UPDATE Accounts SET Balance = ? WHERE num = ?", (balance, num))

    def add_user_to_account(self, num, pin, balance):
        """ This function is only called  during initial set up of game, populates the player db with players. """
        return self.execute("INSERT INTO Accounts (number, pin, balance) VALUES(?, ?, ?)", (num, pin, balance))
    def Select_all(self):
        return self.execute_without("SELECT * FROM Accounts")
    def login(self,num, pin):
        return self.execute("SELECT number from Accounts WHERE number=? AND pin=?", (num, pin))
    def get_balance(self, num):
        return self.cursor.execute("SELECT balance from Accounts WHERE number=?", num)
    def __del__(self):
        """ Destroys instance and connection on completion of called method """
        self.connection.close()
