# Q10. Create a class Member that:
# Has a shared BMI limit for “fit” status.
# Each member stores name, height, weight.
# Has a method to calculate BMI and check fit status.
# Provides a function to update BMI limit for all members.
# Offers a tool to check if height and weight entered are valid numbers.
# Demonstrate:
# 1.Creating multiple members.
# 2.Updating BMI standard.
# 3.Displaying fit status and input validity.
class Member:
    bmi_limit=10
    def __init__(self,n,h,w):
        self.name=n
        self.height=h
        self.weight=w
    def fit_status(self):
        bmi=self.weight//(self.height*2)
    @classmethod
    def update(cls,nw):
        cls.bmi_limit=nw
        pass