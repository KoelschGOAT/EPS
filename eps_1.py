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
<<<<<<< HEAD
        self.menu2 = f"""Logged in as: {self.login_num}
    1. show balance
    2. Logout
    0. Exit

     >> """
=======
>>>>>>> c8646dd3b2e2ce798f5ebcd32dd48dc093c0ca6f

    def create_account(self):
        num = super().create_number()
        pin = super().create_pin()
<<<<<<< HEAD
        super().add_user_to_account(num, pin, super().show_balance())
=======
        EPSDatabase.add_user_to_account(num, pin, super().show_balance())
>>>>>>> c8646dd3b2e2ce798f5ebcd32dd48dc093c0ca6f
        
        print(f"""Account created:
Number: {num}
Pin: {pin}
""")

    def Login(self):
<<<<<<< HEAD
        self.login_num = ""
=======
>>>>>>> c8646dd3b2e2ce798f5ebcd32dd48dc093c0ca6f
        while True:
            num = input("Please Input your Account Number: ")
            pin = input("Please Input your Pin: ")
            num = num.strip()
            pin = pin.strip()
<<<<<<< HEAD
            # Compare input to existing Accounts in Accounts List
            if super().login(num, pin).fetchone():
=======
            # Compare input to existing Accounts in Accounts
            if EPSDatabase.login(num, pin).fetchone():
>>>>>>> c8646dd3b2e2ce798f5ebcd32dd48dc093c0ca6f
                print("Login Successfully")
                self.login_pin = pin
                self.login_num = num
                return True
            else:
                print("Login failed, Account Details invalid")
 
        time.sleep(2)
         
<<<<<<< HEAD

    def Balance(self):
        self.balance = super().get_balance(self.login_num, self.login_pin).fetchall()
        print(f"Your current Balance is: {self.balance[0][0]}€\n")
        time.sleep(2)
        return

    def main(self):
        super().create_table()
        end1 = True
        end2 = True
        while end1:
=======

    def print_Balance(self):
        self.balance = EPSDatabase.get_balance(self.login_num, self.login_pin).fetchall()
        self.balance = round(self.balance[0][0])
        print(f"Your current Balance is: {self.balance}€\n")
        return self.balance


    def transaction(self):
        self.print_Balance()
 
        account_to_send = input(f"Enter an Account you want to send money to: ")
        amount_to_send = input(f"Enter the Amount you want to send: ")
        
        if self.balance - int(amount_to_send) >= 0 and account_to_send != self.login_num:
            if EPSDatabase.get_number(account_to_send).fetchone():
                EPSDatabase.balance_addition(account_to_send, int(amount_to_send))
                EPSDatabase.balance_sub(self.login_num, int(amount_to_send))
                print("transaction Successfully!")
            else: print("Not a valid Account")
        else: print("Invalid amount")
        


    def main(self):
        EPSDatabase.create_table()
        end1 = True
        end2 = True
        while end1:
            end2 = True
>>>>>>> c8646dd3b2e2ce798f5ebcd32dd48dc093c0ca6f
            menu_input = input(self.menu1)
            if menu_input == "1":
                self.create_account()
                continue
            elif menu_input == "2":
                if self.Login():
                    time.sleep(1)
                     
                    while end2:
<<<<<<< HEAD
                        menu2_input = input(self.menu2)
=======
                        menu2_input = input(f"""Logged in as: {self.login_num}
    1. show belence
    2. Logout
    3. Send Money
    0. Exit

     >> """)
>>>>>>> c8646dd3b2e2ce798f5ebcd32dd48dc093c0ca6f
                        if menu2_input == "1":
                            self.print_Balance()
                            continue
                        elif menu2_input == "2":
                            print("You've been logged out")
                            time.sleep(1)
<<<<<<< HEAD
                             
=======
                        
>>>>>>> c8646dd3b2e2ce798f5ebcd32dd48dc093c0ca6f
                            end2 = False
                        elif menu2_input == "3":
                            self.transaction()
                        elif menu2_input == "0":
                            quit()
                        else:
                            print("The Input is invalid")

            elif menu_input == "0":
                quit()
            else:
                print("The Input is invalid")

<<<<<<< HEAD
        
=======
    def __del__(self):
        EPSDatabase.close()
        print("Thank you for using EPS")    
>>>>>>> c8646dd3b2e2ce798f5ebcd32dd48dc093c0ca6f
        
if __name__ == '__main__':

    a = EPSAccount()
    
    a.balance = 49.99
    a.main()
