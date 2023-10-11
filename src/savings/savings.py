from account.account import *

class savings(account):

    def __init__(self, balance, interestRate):
        super().__init__(balance)
        self.__interestRate = interestRate

    def setInterestRate(self, interestRate: float):
        self.__interestRate = interestRate

    def getInterestRate(self):
        return self.__interestRate
    
    def getInterest(self):
        return self.__balance * self.__interestRate
        
    def credit(self, amount: float):
        super().credit(amount * self.__interestRate)

    def __str__(self):
        