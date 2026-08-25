#it is process of protecting the data

#private
#protected
#Public


class Bank:
    def __init__(self,name,balance, accountNO):
        self.name = name #public
        self.__balance = balance #private
        self._accountNO = accountNO #protected

    def displayInfo(self):
        print(self.__balance)

    def deposit(self,amount):
        self.__balance += amount
        print(self.__balance)

    def withdraw(self,amount):
        self.__balance -= amount
        print(self.__balance)


class HDFCBANK(Bank):
    def __init__(self,name,balance,accountNO):
        super().__init__(name,balance,accountNO)

    def displayInfo(self):
        print(self._accountNO)

o = HDFCBANK("Sagar",1233,"0231")
print(o.name)

o.displayInfo()