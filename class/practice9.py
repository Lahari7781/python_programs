# Q9. Create a class BankAccount with:
# class variable bank_name
# instance variables holder and balance
# instance method deposit(amount)
# class method change_bank_name(cls, new_name)
# static method validate_amount(amount) → returns True if amount > 0
# Show transactions and how static + class methods work together.
class BankAccount:
    bank_name="SBI"
    def __init__(self,h,b):
        self.holder=h
        self.balance=b
    def deposit(self,amount):
        if(BankAccount.validate_amount(amount)):
            self.balance+=amount
            return self.balance
    @classmethod
    def change_bank_name(cls,new_name):
        cls.bank_name=new_name
        return cls.bank_name
    @staticmethod
    def validate_amount(amount):
        return amount>0
b1=BankAccount("Hrithik",50000)
print(b1.deposit(40000))
b1.change_bank_name("HDFC")
print(BankAccount.bank_name)
