
# Q9. Design a LibraryMember class that:
# Tracks total active members.
# Each member has a name and books_borrowed count.
# Has a function to borrow books, with borrowing limit common to all.
# Allows updating borrowing limit globally.
# Has a static function to check if book title is valid (non-empty string, reasonable length).
# Demonstrate:
# 1.Borrowing books for multiple users.
# 2.Changing borrowing limits.
# 3.Validating book titles before borrowing.
class Library:
    total=0
    limit=5
    def __init__(self,name):
        self.name=name
        self.books=0
        Library.total+=1
    def books_borrowed(self,nw,title):
        if(Library.valid(title)):
            k=self.books+nw
            if(k<=self.limit):
                self.books=k
                print(f"books borrowed:{self.books}")
            else:
                print("Limit exceeded")
        else:
            print("title is less than 8 charcters")
    @classmethod
    def update(cls,nw):
        cls.limit=nw
        print(f"limit updated:{cls.limit}")
    @staticmethod
    def valid(title):
        return len(title)>8
b1=Library("Rishi")
Library.update(10)
print(f"Library limit chaged to :{Library.limit}")
b1.books_borrowed(3,"Alchemist")