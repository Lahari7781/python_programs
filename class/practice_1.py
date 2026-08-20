class Student:
    def __init__(self,n,m):
        self.name=n
        self.marks=m
    def is_passed(self):
        if(self.marks>40):
            return True
        else:
            return False
s1=Student("Prabas",50)
if s1.is_passed()==True:
    print(f"{s1.name}:Passed")
else:
    print(f"{s1.name}:Falied")
s2=Student("Pratham",30)
if s2.is_passed()==True:
    print(f"{s2.name}:Passed")
else:
    print(f"{s2.name}:Falied")


