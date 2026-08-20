class Bank:
    def __init__(self,n,a,p):
        self.name=n
        self.acc=a
        self.pin=p
        self.balance = 0
    def deposit(self):
        m=int(input("Enter amount to depoist:"))
        if(m>=0):
            self.balance+=m
            print(f"{m} is deposited")
        else:
            print("Invalid entry")
    def withdraw(self):
        if(self.validate()):
            am=int(input("Enter amount to withdraw:"))
            if (am>=0 and am <=self.balance):
                self.balance-=am
                print("{am} is withdrawn")
            else:
                print(f"Enter amount is invalid")
        else:
            print("Enter correct pin")
    def change_pin(self):
        p=int(input("Enter pin:"))
        if(self.validate(p)):
            k=int(input("Enter new pin:"))
            Bank.pin=k
            print("Pin is succefully changed")
    def validate():
        p=int(input("Enter Pin:"))
        if(p==Bank.pin):
            return True
        else:
            return False
    def __str__(self):
        return f"Name:{self.name},acc:{self.acc},balance:{self.balance}"
    def __repr__(self):
        return self.name

b1=Bank("Lahari",532145556,2912)
b2=Bank("Madh",9087645,7539)
b1.deposit()
b1.withdraw()
print(b1)
l=[b1,b2]
print(l)
