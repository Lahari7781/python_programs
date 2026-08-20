# Write a class Vector2D(x, y). Implement __add__, __sub__, __mul__ (scalar
# multiply), __truediv__ (scalar divide), __floordiv__, and __mod__ (element-wise).
# Also add __str__ and __repr__. Test: Vector2D(3,4) + Vector2D(1,2) should give
# Vector2D(4,6).
class Vector:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __add__(self,o2):
        return Vector(self.x+o2.x,self.y+o2.y)
    def __str__(self):
        return f"Vector({self.x},{self.y})"
    def __sub__(self,o2):
        return Vector(self.x+o2.x,self.y-o2.y)
    def __mul__(self,o2):
        return Vector(self.x*o2.x,self.y*o2.y)
    def __truediv__(self,o2):
        return Vector(self.x/o2.x,self.y/o2.y)
    def __floordiv__(self,o2):
        return Vector(self.x//o2.x,self.y//o2.y)
    def __mod__(self,o2):
        return Vector(self.x%o2.x,self.y%o2.y)

v1 = Vector(3, 4)
v2 = Vector(1, 2)
print(v1+v2)
print(v1 - v2)
print(v1*v2)
print(v1/v2)
print(v1//v2)
print(v1%v2)
