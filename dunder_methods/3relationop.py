# Relational Dunders Create a class Temperature(celsius).
# Implement all six relational dunders (__lt__, __le__, __gt__, __ge__, __eq__, __hash__).
# Sort a list of Temperature objects and store them in a set. Verify:
# Temperature(100) > Temperature(50) is True.
class Temperature:
    def __init__(self,temp):
        self.temp=temp
    def __lt__(self,o2):
        return self.temp<o2.temp
    def __le__(self,o2):
        return self.temp<=o2.temp
    def __gt__(self,o2):
        return self.temp>o2.temp
    def __ge__(self,o2):
        return self.temp>=o2.temp
    def __eq__(self,o2):
        return self.temp==o2.temp
    def __hash__(self):
        return hash(self.temp)
t1=Temperature(100)
t2=Temperature(50)
print(t1>t2)
print(t1<t2)
print(t1==t2)
print(t1>=t2)
print(t1<=t2)
