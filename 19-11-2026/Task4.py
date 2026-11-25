from Task3 import Account,InsufficientFundsError

class SavingsAccount(Account): #parent class and child class
    def __int__(self, owner, balance=0, min_balance=500):
        super().__init__(owner,balance)
        self.min_balance=min_balance

#override 

def withdraw(self, amount):
    if self.balance - amount < self.min_balance:
        raise InsufficientFundsError(
            f"Insufficient funds.balance:{self.balance},requested:{amount}")
    self.balance -= amount
    print(f"self.owner withdraw {amount} -> balance {self.balance}")


#test case

priya=SavingsAccount("Priya",1500)

try:
    priya.withdraw(1200)
except InsufficientFundsError as e:
    print(f"error:{e}")

try:
    priya.withdraw(500)
except InsufficientFundsError as e:
    print(f"error:{e}")


print(isinstance(priya,Account))