# Q3. Create an Employee class that:
# Keeps a minimum experience required for promotion (shared across all employees).
# Stores employee name, experience, and department.
# Has a method to check eligibility for promotion.
# Provides a function to update promotion criteria globally.
# Offers a general tool that checks if a given department is valid (like “HR”, “Tech”, “Admin”).
# Demonstrate:
# 1.Creating employees from different departments.
# 2.Changing promotion criteria.
# 3.Displaying eligibility results and department validation.
class Employee:
    min_exp=2
    def __init__(self,n,e,d):
        self.name=n
        self.exp=e
        self.dept=d
    def eligiblity(self):
        if(self.exp>=Employee.min_exp):
            print("Eligible For Promotion")
        else:
            print("Not Eligible For Promotion")
    @classmethod
    def update(cls,new):
        cls.min_exp=new
    # Offers a general tool that checks if a given department is valid (like “HR”, “Tech”, “Admin”).
    @staticmethod
    def validate(dep):
        if(dep=="HR" or dep=="Tech" or dep=="Admin"):
            return "Correct Dept"
        else:
            return "Wrong dept"
# 1.Creating employees from different departments.
e1=Employee("Mahesh",3,"HR")
e1.update(4)
print(Employee.min_exp)
e1.eligiblity()
print(Employee.validate("HR"))


