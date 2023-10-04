from abc import ABC, abstractmethod

class tranaction:
    """The transaction abstract class defines methods that may be
    implemented by an Account class.
    """    
    
    @abstractmethod
    def getBalance(self):
        """Returns the current balance of this account
        """        
        
        pass


    @abstractmethod
    def isEmpty(self):
        """Checks if the balance for this account is zero and returns True
        if the balance is zero, else returns False.
        """        
       
    @abstractmethod
    def credit(self, amount: float):
        """Increases the balance of this account by the specified amount

        Args:
            amount (float): the amount to increase the balance by
        """ 
        pass       

    @abstractmethod
    def debit(self, amount: float):
        """Decreases the balance of this account by the specified amount.

        Args:
            amount (float): the amount to decrease the balance by
        """ 
        pass       
