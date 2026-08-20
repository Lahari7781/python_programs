# Q2. Design a class Product that:
# Maintains a base tax rate applicable to all products.
# Each product has a name and base price.
# Has a method to compute final price including tax.
# Can change tax rate for all products using one method.
# Includes a function to check whether a given price is valid or not (non-negative and realistic).
# Demonstrate:
# 1.Creating multiple products.
# 2.Changing the tax rate.
# # 3.Showing updated prices and
# validity checks.
class Product:
    base_tax=5
    def __init__(self,name,base_price):
        self.name=name
        self.base_price=base_price
    def final_price(self):
        return self.base_price+((Product.base_tax*self.base_price)/100)
    @classmethod
    def change_taxrate(cls,new):
        cls.base_tax=new
    @staticmethod
    def validate_price(price):
        return 0<=price<=1000000
p1=Product("Laptop",50000)
Product.change_taxrate(20)
print(Product.base_tax)
print(p1.final_price())
print(p1.validate_price(20000))