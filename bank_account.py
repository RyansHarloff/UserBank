class BankAccount:
    bank_name = " The best Bank"
    def __init__(self,name, int_rate, balance):
        self.name = name
        self.int_rate = int_rate
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        if BankAccount.can_withdraw(self.balance,amount):
            self.balance -= amount
        else:
            print("Insufficient Funds, Charging a $5 fee.")
        return self
    def display_account_info(self):
        print(self.balance)
        return self

    @staticmethod
    def can_withdraw(balance,amount):
        if(balance - amount) <0:
            return False
        else:
            return True

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(name,0.02,0)
    def make_deposit(self):
        self.account.deposit(350)
        print(self.account.balance)
    def make_withdraw(self):
        self.account.withdraw(150)
        print(self.account.balance)
    def display_user_balance(self):
        self.account.display_account_info
        print(self.account.balance)


Dave = User("Dave","Dave@me.com")
James = User("James","james@me.com")

Dave.make_deposit()
Dave.make_withdraw()
Dave.display_user_balance()