
from abc import ABC,abstractmethod

class bank(ABC):
    
    @abstractmethod
    def check_balance(self):
        pass
    
    @abstractmethod
    def depo_balance(self):
        pass

    @abstractmethod
    def wid_balance(self):
        pass

class gpay(bank):

    def __init__(self):
        self.balance = 1000
    
    def check_balance(self):
        return "Current balance is " + str(self.balance)

    def depo_balance(self,depo):
        self.balance = self.balance + depo

    def wid_balance(self,wid):
        self.balance = self.balance - wid


google = gpay()

print(google.check_balance())
google.depo_balance(500)
print(google.check_balance())
google.wid_balance(200)
print(google.check_balance())

class phonepay(bank):

    def __init__(self):
        self.balance = 2000
        self.wallet = 0

    def check_balance(self,bal):
        if bal == "account":

            return "Current balance in account is " + str(self.balance)

        elif(bal=="wallet"):
            return "Current balance in wallet is " + str(self.wallet)
    def depo_balance(self,depo):
        self.balance = self.balance + depo

    def wid_balance(self,wid):
        self.balance = self.balance - wid

    def add_wallet(self,add):
        self.wallet = self.wallet + add

google1 = phonepay()
print(google1.check_balance("account"))
print(google1.check_balance("wallet"))
google1.add_wallet(500)
print(google1.check_balance("wallet"))