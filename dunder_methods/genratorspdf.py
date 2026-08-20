# 1.Write a generator that yields numbers from 1 to N.
def Num(n):
    for i in range(n):
        yield i
for i in Num(20):
    print(i)