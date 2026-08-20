class Book:
    total_books=0
    def __init__(self,t,a):
        self.title=t
        self.author=a
        Book.total_books+=1
    @staticmethod
    def is_valid_title(title):
        return len(title)>=3
    @classmethod
    def from_string(cls,book_str):
        t,a=book_str.split("-")
        if(cls.is_valid_title(t)==True):
            b=cls(t,a)
            return b
#calling using constructor is_valid_title
if(Book.is_valid_title("It Starts with us")):
    b1=Book("It Starts with us","coolen hover")
print(b1.title+"-"+b1.author)
#calling using
b2=Book.from_string("At-James Clear")
if b2:
    print(b2.title+"-"+b2.author)
else:
    print("Nothing is object")
print(Book.total_books)


