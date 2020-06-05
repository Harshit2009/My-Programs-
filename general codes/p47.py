class BankAccount :
    account_type = 'Bank Account'
    def __init__(self,name,balance):
        
        self.name = name
        self.balance = balance
    def __init__(self,name,balance,accno,sortcode,bankname) :
        Account.__init__(self,name,balance)
        self.accno = accno
        self.sortcode = sortcode
        self.bankname = bankname
class CreditCard:
    accont_type = 'Credit Card'
    def __init__(self,name,balance,accno,expiry,limit,rate) :
        Account.__init__(self,name,balance)
        self.accno = accno
        self.expiry = expiry
        self.limit = limit
        self.rate = rate
    def withdraw(self,amount) :
        if abs(self.balance - amount) < self.limit :
            self.balnce -= amount
        else :
                raise ValueError
    def add_interest(self) :
        self.balance -= ((abs(self.balance)*(self.rate/100))/12)
        
z1= BankAccount('Harshit',6789,567,123,'SBI')

