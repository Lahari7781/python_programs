class A:
    def __init__(self,str):
        self.str=str
        self.index=0
    def __iter__(self):
        return self
    def __next__(self):
        while(self.index<len(self.str)):
            i=self.index
            self.index += 1
            if(self.str[i] in "AEIOUaeiou"):
                ch= self.str[i]
                return ch
        raise StopIteration
a1=A("werthgsnjklai")
for i in a1:
    print(i)