# Q4. Build a Loan class that:
# Has a common interest rate for all loans.
# Each object stores borrower name and principal.
# Calculates total payable amount.
# Provides a function to update the interest rate.
# Provides a static function to check loan eligibility (e.g., salary > certain threshold).
# Demonstrate:
# 1.Creating multiple loan accounts.
# 2.Updating interest rates.
# 3.Checking eligibility and total repayment for borrowers.
class Loan:
    rate_int=5
    def __init__(self,name,p):
        self.name=name
        self.principal=p
    def total(self):
        I=(self.principal*self.rate_int)/100
        amount=self.principal+I
        return amount
    @classmethod
    def change_rate(cls,nw):
        cls.rate_int=nw
    @staticmethod
    def eligible(salary):
        if(salary)>100000:
            return "Eligible"
        else:
            return "Not Eligible"
l1=Loan("Nani",20000)
print(l1.total())
Loan.change_rate(10)
print(Loan.rate_int)
print(l1.total())
print(Loan.eligible(20000))

