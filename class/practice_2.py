# Q2. Create a class Employee with attributes name and company_name = "TechCorp".
# Add a class method change_company(cls, new_name) to update the company name for all employees.
class Employee:
    company_name="TechCorp"
    def __init__(self,n):
        self.name=n
    @classmethod
    def change_method(cls,new_name):
        Employee.company_name=new_name
e1=Employee("Lahari")
print(f"Before change :{e1.company_name}")
e1.change_method("google")
print(f"After change:{e1.company_name}")