class vector:
    def __init__(self,a,b):
        self.first=a
        self.second=b
    def __add__(self,other):
        return vector(self.first+other.first,self.second+other.second)
    def __sub__(self,other):
        return self.first-other.first-self.second-other.second
    def __str__(self):
        return f"{self.first},{self.second}"
    def __repr__(self):
        return f"{self.first},{self.second}"
v1=vector(7,8)
v2=vector(6,7)
v3=vector(3,4)
print(v1+v2)
print(v1-v2)
print(v1)
l=[v1,v2]
print(l)
print(v1+v2+v3)