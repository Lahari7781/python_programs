# Q5.Create a class Temperature with:
# instance attribute celsius
# a static method to_fahrenheit(celsius)
# an instance method show_conversion() that uses the static method to print both values.
class Temperature:
    def __init__(self,cel):
        self.celsius=cel
    @staticmethod
    def to_fahrenheit(cel):
        return (cel*(9/5))+32
    def show_conversion(self):
        f=Temperature.to_fahrenheit(self.celsius)
        print(f"Before Value:{self.celsius}C")
        print(f"after conversion:{f}F")

t1=Temperature(30)
t1.show_conversion()




