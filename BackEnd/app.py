class BankAccount(object):
    balance = 0
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"{self.name}'s account has a balance of ${self.balance:.2f}"

    def show_balance(self):
        print(f"Total balance is ${self.balance:.2f}")

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit must be a positive value")
            return
        else:
            print(f"Depositing ${amount:.2f}")
            self.balance += amount
            self.show_balance()
    def withdraw(self, amount):
        if amount > self.balance:
            print("Not enough money in account")
        else:
            print(f"Withdrawing ${amount:.2f}")

            self.balance -= amount
            self.show_balance()

myaccount = BankAccount("Oscar")
myaccount.deposit(2000)
myaccount.withdraw(200)
myaccount.withdraw(3000)
myaccount.show_balance()


print("REPO TEST")




