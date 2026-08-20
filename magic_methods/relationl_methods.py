
class Student:
    def __init__(self,id,n,m):
        self.id=id
        self.name=n
        self.marks=m
    def __eq__(self,other):
        return self.marks==other.marks
    def __gt__(self,other):
        return self.marks>other.marks
    def __lt__(self,other):
        return self.marks<other.marks
    def __repr__(self):
        return f"{self.marks}"
    def __hash__(self):
        return self.marks
s1=Student(25,"sa",100)
s2=Student(30,"Si",100)
s3=Student(1,"Ma",100)
print(s1>s2)
print(s2>s3)
print(s1==s2)
l={s1,s2,s3}
print(l)
