from math import pi
class circle:
    def __init__(self,r):
        self.radius=r
    def area(self):
        return ((pi)*(self.radius**2))
    def perimeter(self):
        return 2*(pi)*self.radius
    def describe(self):
        print(f"{self.area()},{self.perimeter()}")
c1=circle(7)
c1.describe()
