class emp:
    def __init__(self,n,e,s):
        self.name=n
        self.exp=e
        self.salary=s
    def __str__(self):
        return f"NAME:{self.name}"
e1=emp("lahari",2,100000)
print(e1)