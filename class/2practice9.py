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
class LibraryMember:
    total=0
    limit=5
    def __init__(self,name):
        self.name=name
        self.books=0
        LibraryMember.total+=1
    def borrow_books(self,nw,title):
        if(LibraryMember.check_title(title)):
            k=self.books+nw
            if(k<=self.limit):
                self.books=k
                print(self.books)
            else:
                print("books Limit Excceded")
        else:
            print("Title is less than 8 charcters")
    @classmethod
    def update_limit(cls,nw):
        cls.limit=nw
    @staticmethod
    def check_title(title):
        return len(title)>8
b1=LibraryMember("Rishi")
LibraryMember.update_limit(10)
print(f"Library limit chaged to :{LibraryMember.limit}")
b1.borrow_books(3,"Alchemist")

