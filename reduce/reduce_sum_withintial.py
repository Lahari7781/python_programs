from functools import reduce
l=[1,2,3,4]
k=reduce(lambda x,y:x+y,l,10)
print(k)