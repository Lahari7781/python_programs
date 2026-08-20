# Q3. Create a class MathOps with a static method is_even(num) that returns True if the number is even.
# Then call it both from the class and an instance.
class MathOps:
    @staticmethod
    def is_even(num):
        return num%2==0
o=MathOps()
#calling form static method
print(MathOps.is_even(15))
#calling from instance method
print(o.is_even(20))
