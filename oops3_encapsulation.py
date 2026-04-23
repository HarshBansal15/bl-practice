class bank:
    def __init__(self,balance,accno):
        self.balance=balance
        self.accno=accno

    def debit(self,amount):
        self.balance-=amount
    def credit(self,amount):
        self.balance+=amount
    def update(self):
        print("Your updated balance is : " ,self.balance)


accno=int(input("Enter accno : "))
balance=int(input("Enter balance : "))
c1=bank(balance,accno)
update=input("Enter d for debit or c for credit ")
if (update=='d'):
    a1=int(input("Enter amount"))
    c1.debit(a1)
else :
    a1=int(input("Enter amount"))
    c1.credit(a1)

c1.update()


        