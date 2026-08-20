#create student class with name,sec,maths,phy,chem as attributes .an instance method to calculate
#total marks and return them .an instance /static method provide grade A,B,C,D,E
#print(s1) gives name:totalmarks:grade,l=[s1,s2,s3] print [name,grade....]
class Student:
    def __init__(self,n,s,m,p,c):
        self.name=n
        self.section=s
        self.maths=m
        self.phy=p
        self.chem=c
    def total(self):
        return self.maths+self.phy+self.chem
    @staticmethod
    def grade(k):
        if(k>=90):
            return "A"
        elif(80<=k<90):
            return "B"
        elif(70<=k<80):
            return "C"
        elif(60<=k<50):
            return "D"
        else:
            return "E"
    def __str__(self):
        return f"NAME:{self.name}\nTotal Marks:{self.total()}\nGrade={self.grade(self.total()//3)}"
    def __repr__(self):
        return f"NAME,GRADE:{self.name},{self.grade(self.total()//3)}"
s1=Student("Lahari","Alpha",50,60,70)
s2=Student("Madhuri","Beta",60,70,80)
s3=Student("Madhu","Beta",60,70,80)
print(s1)
l=[s1,s2,s3]
print(l)