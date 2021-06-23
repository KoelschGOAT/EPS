import sqlite3
import os
import time



class EPSDatabase:
    connection = sqlite3.connect(os.path.join("eps_database.db"))
    cursor = connection.cursor()

    @staticmethod
    def execute(query, data):
        EPSDatabase.cursor.execute(query, data)
        EPSDatabase.connection.commit()
        return EPSDatabase.cursor

    @staticmethod
    def execute_query(query):
        EPSDatabase.cursor.execute(query)
        EPSDatabase.connection.commit()
        return EPSDatabase.cursor
    @staticmethod
    def create_table():
        return EPSDatabase.execute_query("CREATE TABLE IF NOT EXISTS Accounts(id INTEGER PRIMARY KEY AUTOINCREMENT, number Text, pin TEXT, balance Decimal(6,2) DEFAULT 0)")

    @staticmethod
    def print_table():
        return EPSDatabase.execute("SELECT * FROM Accounts")

    @staticmethod
    def add_user_to_account(num, pin, balance):
        return EPSDatabase.execute("INSERT INTO Accounts (number, pin, balance) VALUES(?, ?, ?)", (num, pin, balance))

    @staticmethod
    def Select_latest():
        return EPSDatabase.execute_query("SELECT number FROM Accounts ORDER BY number DESC LIMIT 1")

    @staticmethod
    def login(num, pin):
        return EPSDatabase.execute("SELECT number from Accounts WHERE number=? AND pin=?", (num, pin))

    @staticmethod
    def get_balance(num, pin):
        return EPSDatabase.execute("SELECT balance FROM Accounts WHERE number=? AND pin=?", (num, pin))

    @staticmethod
    def get_number(num):
        return EPSDatabase.execute("SELECT number FROM Accounts WHERE number=?", (num,))
    @staticmethod
    def balance_addition(num, balance):
        return EPSDatabase.execute("UPDATE Accounts SET balance = balance + ? WHERE number = ?", (balance, num))
    @staticmethod
    def balance_sub(num, balance):
        return EPSDatabase.execute("UPDATE Accounts SET balance = balance - ? WHERE number = ?", (balance, num))

    @staticmethod
    def close():
        EPSDatabase.connection.close()


if __name__ == '__main__':
    a = DatabaseInterface()
    print(a.Select_latest())
