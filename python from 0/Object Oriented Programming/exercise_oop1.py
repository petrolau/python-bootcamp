# Define Bank Account Below:
class BankAccount:
    def __init__(self,owner,balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self,number):
        self.balance += number
        return self.balance

    def withdraw(self,number):
        self.balance -= number
        return self.balance 

acct = BankAccount("Darcy")
print(acct.owner)
print(acct.balance)
acct.deposit(10)
acct.withdraw(3)
print(acct.balance)


