class Account(object):

    def __init__(self, name, balance):
        self.__name = name
        self.__balance = balance


    def deposit(self, amount):
        self.__balance += amount


    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount

    def getBalance(self):
        return self.__balance


    def getName(self):
        return self.__name




class CheckingAccount(Account):
    def __init__(self, name , balance ,  minBalance = 500   ):
        super().__init__(name , balance)
        self.__minBalance = minBalance
    
    def withdraw(self, amount ):
        if super().getBalance() - amount >= self.__minBalance:
            super().withdraw(amount)
            print("Okay")
        else:
            print(f"Please keep balance above ${self.__minBalance}.")








a = CheckingAccount("affan" , 700)
a.withdraw(50)
a.withdraw(50)
a.withdraw(50)
a.withdraw(50)
a.withdraw(50)
a.withdraw(50)
a.withdraw(50)
a.withdraw(50)
a.withdraw(50)
a.deposit(500)
a.withdraw(50)
a.withdraw(50)

print(  a.getBalance()     )