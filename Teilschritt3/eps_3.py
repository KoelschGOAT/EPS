from eps_base import Account
import sqlite3
import time
from database import EPSDatabase


class EPSAccount(Account):
    def __init__(self):
        super().__init__()

        self.login_num = ""
        self.login_pin = ""
        self.menu1 = """Willkommen in EPS:
    1. Create Account
    2. Login Account
    0. Exit

    >> """

    def create_account(self):
        num = super().create_number()
        pin = super().create_pin()
        EPSDatabase.insert_data(num, pin, super().show_balance())

        print(f"""Account created:
Number: {num}
Pin: {pin}
""")

    def Login(self):
        while True:
            num = input("Please Input your Account Number: ")
            num = num.zfill(8)
            pin = input("Please Input your Pin: ")
            num = num.strip()
            pin = pin.strip()
            #print(EPSDatabase.login(num, pin).fetchone())
            # Compare input to existing Accounts in Accounts
            if EPSDatabase.login(num, pin).fetchone():
                print("Login Successfully")
                self.login_pin = pin
                self.login_num = num
                return True
            else:
                print("Login failed, Account Details invalid")

        

    def print_Balance(self):
        self.balance = EPSDatabase.get_balance(
            self.login_num, self.login_pin).fetchall()
        self.balance = round(self.balance[0][0], 2)
        print(f"Your current Balance is: {self.balance}€\n")
        return self.balance

    def transaction(self):
        self.print_Balance()

        account_to_send = input(
            f"Enter an Account you want to send money to: ")
        while True:
            try:
                amount_to_send = int(input(f"Enter the Amount you want to send: "))
                break
            except ValueError:
                print("No Number entered")
                continue
        account_to_send = account_to_send.zfill(8)
        if self.balance - amount_to_send >= 0 and account_to_send != self.login_num:
            if EPSDatabase.get_number(account_to_send).fetchone():
                EPSDatabase.balance_addition(
                    account_to_send, int(amount_to_send))
                EPSDatabase.balance_sub(self.login_num, int(amount_to_send))
                print("transaction Successfully!")
                self.print_Balance()

            else:
                print("Not a valid Account")
        else:
            print("Invalid amount")

    def add_balance(self):
        amount_to_add = input(f"Enter the amount you want to add: ")
        EPSDatabase.balance_addition(self.login_num, int(amount_to_add))
        self.print_Balance()

    def delete_account(self):
        EPSDatabase.del_account(self.login_num)

    def main(self):
        EPSDatabase.create_table()
        end1 = True
        end2 = True
        while end1:
            end2 = True
            menu_input = input(self.menu1)
            if menu_input == "1":
                self.create_account()
                continue
            elif menu_input == "2":
                if self.Login():
                    time.sleep(1)

                    while end2:
                        menu2_input = input(f"""Logged in as: {self.login_num}
    1. eps Account Balance
    2. Add Money
    3. transfer Money
    4. Delete Account
    5. Log out
    0. Exit

     >> """)
                        if menu2_input == "1":
                            self.print_Balance()
                        elif menu2_input == "2":
                            self.add_balance()
                        elif menu2_input == "3":
                            self.transaction()
                        elif menu2_input == "4":
                            self.delete_account()
                            end2 = False
                        elif menu2_input == "5":
                            print("You've been logged out")
                            time.sleep(1)
                            end2 = False
                        elif menu2_input == "0":
                            quit()
                        else:
                            print("The Input is invalid")

            elif menu_input == "0":
                quit()
            else:
                print("The Input is invalid")

    def __del__(self):
        EPSDatabase.close()
        print("Thank you for using EPS")


if __name__ == '__main__':

    a = EPSAccount()

    a.balance = 49.99
    a.main()
