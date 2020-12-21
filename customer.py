from atm_card import ATMCard

class Customer:
    def __init__(self, id, custPin, custBalance):
        self.id = id
        self.custPin = custPin
        self.custBalance = custBalance

    def getID(self):
        return self.id
    
    def getCustPin(self):
        return self.custPin

    def getCustBalance(self):
        return self.custBalance

    def withdraw(self, nominal):
        self.custBalance -= nominal 
        return self.custBalance 

    def deposit(self, nominal):
        self.custBalance += nominal
        return self.custBalance

    def changeNewPin(self, newcustPin):
        self.custPin = newcustPin