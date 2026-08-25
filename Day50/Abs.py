from abc import ABC, abstractmethod

class Bank(ABC):
    @abstractmethod
    def deposit(self,amount):
        pass

    @abstractmethod
    def withdraw(self,amount):
        pass


#concrete is implementation class
class HDFCBank(Bank):
    def __init__(self, name, accountNo, balance):
        self.name = name
        self.accountNo = accountNo
        self.balance = balance


    def deposit(self,amount):
        self.balance += amount
        print(self.balance)

    def withdraw(self,amount):
        self.balance -= amount
        print(self.balance)


obj = HDFCBank("Sagar",10000,123456)
obj.deposit(10)
obj.withdraw(5)
