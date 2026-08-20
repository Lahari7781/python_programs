# __len__ and __contains__ Build a class Library with a list of book titles.
# Implement __len__ (number of books), __contains__ (check if a title is in the library),
# and __str__ (returns 'Library with N books'). Test all three methods including bool()
# on an empty library.
class Library:
    def __init__(self,t):
        self.title=t
    def __len__(self):
        return len(self.title)
    def __contains__(self,b):
        return b in self.title
l1=Library(["Atomic","alchem"])
print(len(l1))
print("alchem" in l1)
