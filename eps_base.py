import secrets
import string
from database import EPSDatabase



class Account():
    def __init__(self):
       
        self.ban = 0
        self.pin = 0
        self.balance = 0.0
        self.counter = 0
        self.choice = ""
    def create_pin(self):
        pin = ""
        while len(pin) != 4:
            pin = ''.join((secrets.choice(string.digits) for i in range(4)))
        self.pin = pin
        return self.pin

    def create_number(self):
        number = EPSDatabase.Select_latest().fetchall()
        if number != None:
            if len(number) != 0:
                number = int(number[0][0])
                self.counter = number
        
        ban = self.counter+1
        self.counter += 1
        ban = str(ban)
        ban = ban.zfill(8)
        self.ban = ban
        return self.ban

    def show_balance(self):
        #print(self.balance)
        return self.balance

    
if __name__ == "__main__":
    a = Account()
    print(a.create_number())
    print(a.create_pin())
    print(f"Your Current Balance: {a.show_balance()}€")
    
    #print(f"Your Current Balance: {a.show_balance()}€")
