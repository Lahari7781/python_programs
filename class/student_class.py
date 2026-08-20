class student:
    batch="PYBATCH16"
    total=0
    def __init__(self,n,a,g):
        self.name=n
        self.age=a
        self.gender=g
        student.total+= 1
        print(self.name)
        self.total=self.total+1
s1=student("Lahari",21,"female")
# print(s1.name)
s2=student("Madhuri",23,"Female")
s3=student("Madhu",23,"male")
s4=student("Vishu",23,"male")
s5=student("kali",23,"Female")
print(student.total)
print(student.batch)
print(s1.__dict__)
print(student.__dict__)
print(s1.__init__)
print(s1.batch)
print(student.batch)