import sqlite3
import os



class Database:
    def __init__(self):
        self.connection = sqlite3.connect(os.path.join("eps_database.db"))
        self.cursor = self.connection.cursor()

    def execute(self, query, data):
        self.cursor.execute(query, data)
        self.connection.commit()
        return self.cursor

    def execute_query(self, query):
        self.cursor.execute(query)
        self.connection.commit()
        return self.cursor

    def create_table(self):
        return self.execute_query("CREATE TABLE IF NOT EXISTS Accounts(id INTEGER PRIMARY KEY AUTOINCREMENT, number Text, pin TEXT, balance Decimal(6,2) DEFAULT 0)")

    def print_table():
        return self.execute_query("SELECT * FROM Accounts")

    def add_user_to_account(self, num, pin, balance):
        return self.execute("INSERT INTO Accounts (number, pin, balance) VALUES(?, ?, ?)", (num, pin, balance))

    def Select_latest(self):
        return self.execute_query("SELECT number FROM Accounts ORDER BY number DESC LIMIT 1")

    def login(self, num, pin):
        return self.execute("SELECT number from Accounts WHERE number=? AND pin=?", (num, pin))

    def get_balance(self, num, pin):
        return self.cursor.execute("SELECT balance from Accounts WHERE number=? AND pin=?", (num, pin))

    def __del__(self):
        print("closed")
        self.connection.close()


if __name__ == '__main__':
    a = DatabaseInterface()
    print(a.Select_latest())
"""
    def change_balance(self, num, balance):
        return self.execute("UPDATE Accounts SET Balance = ? WHERE num = ?", (balance, num))
"""
