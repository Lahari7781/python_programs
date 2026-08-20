class Book:
    total_books=0
    def __init__(self,n,a):
        self.name=n
        self.author=a
    @classmethod
    def creation(cls,n,a):
        if(len(n)>=5):
            cls.update(30)
            return cls(n,a)
        else:
            return "This is too short"
    @classmethod
    def update(cls,nt):
        cls.total_books=nt
        print(f"Total book:{cls.total_books}")
b1=Book.creation("The Autor","author")
print(b1.name)
