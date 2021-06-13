from esp_base import Account
import os
import time
import keyboard

class EPSAccount(Account):
    _account_list = []
    _balance_list = []
    def create_account(self):
        num = Account.create_number(self)
        pin = Account.create_pin(self)
        self._account_list.append((num,pin))
        self._balance_list.append((num,self.balance))
        #print(f"Accounts: {self._account_list}")
        #print(f"Account balances: {self._balance_list}")
        os.system('cls')
        print(f"""Account created:
Number: {num}
Pin: {pin}
""")
        
    
    def Login(self):
        self.login_num = ""
        if len(self._account_list) > 0:
            while True:
                num_input = input("Please Input your Account Number: ")
                pin_input = input("Please Input your Pin: ")
                #Compare input to existing Accounts in Account List
                for index, item in enumerate(self._account_list):
                    if item[0] == num_input:
                        if item[1] == pin_input:
                            print("Login Login successfull")
                            self.login_num = num_input
                            return True
                        
                print("Login failed, Account Details invalid")
        print("No Account created")
        time.sleep(2)
        os.system('cls')

    def Balance(self):
        if self.login_num != "":
            for index, item in enumerate(self._balance_list):
                if item[0] == self.login_num:
                   print(f"Your current Balance is: {item[1]}\n")
                   time.sleep(2)
                   return
        
    def main(self):
        end1 = True
        end2 = True
        while end1:
            menu_input = input("""Willkommen in EPS:
1. Create Account
2. Login Account
0. Exit

 >> """)
            if menu_input == "1":
                self.create_account()
                continue
            elif menu_input == "2":
                if self.Login():
                    time.sleep(1)
                    os.system('cls')
                    while end2:
                        menu2_input = input(f"""Logged in as: {self.login_num}
1. show balance
2. Logout
0. Exit

>> """)
                        if menu2_input == "1":
                            self.Balance()
                            continue
                        elif menu2_input == "2":
                            print("You've been logged out")
                            time.sleep(1)
                            os.system('cls')
                            end2 = False
                        elif menu2_input == "0":
                            os.system("cls")
                            print("Thank you for using EPS")
                            quit()
                        else:
                            print("The Input is invalid")

            elif menu_input == "0":
                os.system("cls")
                print("Thank you for using EPS")
                quit()
            else:
                print("The Input is invalid")
if __name__ == '__main__':
    a = EPSAccount()
    a.main()