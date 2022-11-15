



class Bank:
    def __init__(self, name, bank, account):
        self.name = name
        self.balance = 1000
        self.bank = bank 
        self.account = account
    
        
    
    def getname(self):
        return self.name
    
    def getbalance(self):
        return self.balance
    
    def getbank(self):
        return self.bank
    def getaccount(self):
        return self.account
    
    
    # TESTING TO SEE WHATS WRONG WITH THE WITHDRAWING NOT WORKING 
    # Works properly now.
    # (Implement error testing so user doesn't enter string or a negative value.)
    def withdraws(self, amount):
        
        if self.balance > 0 and self.balance >= amount:
            self.balance = self.balance - amount
            return True
        else:
            return False
    
    
    # Deposit fucntion 
    def Deposit(self, amount):
        
        if amount > 0:
            self.balance = self.balance + amount
            return True
        else:
            return False
     
    
if __name__ == '__main__':
    wallet = []
    wallet.append(Bank('ryan', 'Pnc Bank', '123'))
    wallet.append(Bank('alli', 'Pnc Bank', '124'))
    wallet.append(Bank('grecia','Pnc Bank', '125'))
    print(wallet[0].getname())