
class ATM:
    def __init__(self,name,age,accNo,balance):
        self.name = name
        self.age = age
        self.accNo = accNo
        self.balance = balance

    def displayBal(self):
        print(self.balance)

    def withdraw(self,amount):
        balance = self.balance - amount
        print(balance)

    def deposit(self,amount):
        balance = self.balance + amount
        print(balance)



class Machine:
    def __init__(self,name,age,accNo,balance):
        self.name = name
        self.age = age
        self.accNo = accNo
        self.balance = balance

    def displayName(self):
        print(self.name)