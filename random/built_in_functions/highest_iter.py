class A:
    def __init__(self,l):
        self.l=l
        self.i=0
        self.m=self.l[0]
    def __iter__(self):
        return self
    def __next__(self):
        if(self.i<len(self.l)):
            k=self.i
            self.i+=1
            if(self.m<=self.l[k]):
                self.m=self.l[k]
                return self.l[k]
            return self.m
        raise StopIteration
a1=A([7,3,4,8,9,2,10,7,3])
for i in a1:
    print(i)