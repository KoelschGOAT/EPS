import secrets
import string


class Account():
    def __init__(self):
        self.ban = 0
        self.pin = 0
        self.balance = 0
        self.counter = 0
        self.choice = ""

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