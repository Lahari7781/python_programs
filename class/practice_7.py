class Employee:
    bonus_rate=0.1
    def __init__(self,name,base_sal):
        self.name=name
        self.base_salary=base_sal
    def final_salary(self):
        return self.base_salary+(self.base_salary*self.bonus_rate)
    @classmethod
    def update_bonus(cls,new_rate):
        Employee.bonus_rate=new_rate
    @staticmethod
    def is_valid(sal):
        return sal>0
e1=Employee("Ram",1000000)
print(f"{e1.name} final salary is  {e1.final_salary()}")
e1.update_bonus(0.2)
print(f"Updated Bonus Rate:{e1.bonus_rate}")
e2=Employee("Arjun",5000000)
print(f"{e2.name} final salary is {e2.final_salary()}")
e2.update_bonus(0.3)
print(f"Uptaed bonus rate:{e2.bonus_rate}")
