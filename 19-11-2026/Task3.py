#exception class
class InsufficientFundsError(Exception):
    """custom error raised when the isn't enough money"""
pass

#account,withdrawl,deposite class

class Account:
    def __init__(self,owner,balance=0):
        self.owner=owner
        self.balance=balance
    def deposite(self,amount):
        self.balance += amount
        print(f"{self.owner} deposite{amount} -> balance{self.balance}")
    def withdraw(self,amount):
        if amount > self.balance:
            raise InsufficientFundsError(
                f"insufficient funds: balance{self.balance},requested{amount}")
        self.balance -=amount

        print(f"{self.owner} withdraw{amount} ->balance{self.balance}")

    def show(self):
        print(f"owner:{self.owner},balance:{self.balance}")


#test

arun = Account("arun",1000)

try:
    arun.deposite(500)
    arun.withdraw(2000)
except InsufficientFundsError as e:
    print(f"error:{e}")
finally:
    print("Transaction Finished")