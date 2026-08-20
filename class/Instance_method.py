class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner=owner
        self.balance=balance
        self.transactions = []
    def deposit(self, amount):#instance method
               self.balance += amount
               self.transactions.append(('deposit', amount))
               return self.balance
    def withdraw(self, amount):# instance method
               if amount > self.balance:
                   raise ValueError('Insufficient funds')
               self.balance -= amount
               self.transactions.append(('withdraw', amount))
               return self.balance
    def get_summary(self): # instance method
               return f'{self.owner}: Rs.{self.balance}'
acc = BankAccount('Alice', 1000)
acc.deposit(500)
acc.withdraw(200)
print(acc.get_summary())
print(acc.transactions)