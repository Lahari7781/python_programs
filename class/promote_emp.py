class Employee:
    def __init__(self,Name,Exp,Sal,Dep):
        self.name=Name
        self.exp=Exp
        self.sal=Sal
        self.dep=Dep
        self.check_Eligible()
    def promote(self):
        if(self.dep=="emp"):
            self.dep="manager"
        elif(self.dep=="manager"):
            self.dep="HR"
        elif(self.dep=="HR"):
            self.dep="Admin"
        self.sal+=10000
        print(self.sal)
        print(self.dep)
    def check_Eligible(self):
        if(self.exp>=5):
            self.promote()
        else:
            print("Not Promoted")
e=Employee("Lahari",8,10000,"emp")