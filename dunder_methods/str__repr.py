# __str__ and __repr__
# Create a class Book with attributes title, author, and price. Define __str__ to return:
# 'Title by Author — Rs.Price' and __repr__ to return: "Book('Title', 'Author', Price)".
# Verify both using print(), repr(), and in an f-string
class Book:
    def __init__(self,t,a,p):
        self.title=t
        self.author=a
        self.price=p
    def __str__(self):
        return f"{self.title} by {self.author} - {self.price}"
    def __repr__(self):
        return f"Book('{self.title}','{self.author}',{self.price}"
b1=Book("Too good to be True","prajakta",1000)
b2=Book("Atomic Habits","James Clear",300)
b={b1,b2}
print(b1)
print(b)
