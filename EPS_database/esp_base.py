import secrets
import string
import sqlite3

class Account:
    def __init__(self):
        self.ban = 0
        self.pin = 0
        self.balance = 0
        self.counter = 0
        self.choice = ""
        self.connection = sqlite3.connect("User.db")
        self.cursor = self.connection.cursor()
    def create_pin(self):
        pin = ""
        breakk = True
        while len(pin) != 4:
            pin = ''.join((secrets.choice(string.digits) for i in range(4)))
        self.pin = pin
        return self.pin

    def create_number(self):
        ban = self.counter+1
        self.counter += 1
        ban = str(ban)
        ban = ban.zfill(8)
        self.ban = ban
        return self.ban

    def show_balance(self):
        print(self.balance)
        return self.balance
    def add_to_balance(self):
        while True:
            try:
                amount_to_add = float(input("Please Enter the Amount you want to add in Euros: "))
                break
            except Exception:
                print("Invalid input")
        self.balance += amount_to_add
        return self.balance
    def execute(self, query, data):
        self.cursor.execute(query, data)
        self.connection.commit()
        return self.cursor

    def execute_table(self, query):
        self.cursor.execute(query)
        self.connection.commit()
        return self.cursor

    def create_table(self):
        return self.execute("CREATE TABLE IF NOT EXISTS Accounts(Personal_Number TEXT PRIMARY KEY NOT NULL, PIN TEXT, Balance Decimal(6,2))")

    def change_balance(self, ban, balance):
        """ Assigns a league_id to a user which is a foreign key """
        return self.execute("UPDATE Accounts SET Balance = ? WHERE ban = ?", (balance, ban))

    def add_user_to_account(self, ban, pin, balance):
        """ This function is only called  during initial set up of game, populates the player db with players. """
        return "INSERT INTO Accounts (Personal_Number, PIN, Balance) VALUES(?, ?, ?)", (ban, pin, balance)

    def __del__(self):
        """ Destroys instance and connection on completion of called method """
        self.connection.close()
if __name__ == "__main__":
    a = Account()
    print(a.create_number())
    print(a.create_pin())
    print(f"Your Current Balance: {a.show_balance()}€")
    a.add_to_balance()
    print(f"Your Current Balance: {a.show_balance()}€")
