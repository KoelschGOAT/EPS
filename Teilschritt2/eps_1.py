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
        self.menu2 = f"""Logged in as: {self.login_num}
    1. show balance
    2. Logout
    0. Exit

     >> """

    def create_account(self):
        num = super().create_number()
        pin = super().create_pin()
        EPSDatabase.add_user_to_account(num, pin, super().show_balance())
        
        print(f"""Account created:
Number: {num}
Pin: {pin}
""")

    def Login(self):
        self.login_num = ""
        while True:
            num = input("Please Input your Account Number: ")
            pin = input("Please Input your Pin: ")
            num = num.zfill(8)
            num = num.strip()
            pin = pin.strip()
            # Compare input to existing Accounts in Accounts
            if EPSDatabase.login(num, pin).fetchone():
                print("Login Successfully")
                self.login_pin = pin
                self.login_num = num
                return True
            else:
                print("Login failed, Account Details invalid")
 
        
         

    def print_Balance(self):
        self.balance = EPSDatabase.get_balance(self.login_num, self.login_pin).fetchall()
        print(f"Your current Balance is: {round(self.balance[0][0],2)}€\n")
        return self.balance


    
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
    1. show belence
    2. Logout
    0. Exit

     >> """)
                        if menu2_input == "1":
                            self.print_Balance()
                            continue
                        elif menu2_input == "2":
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
