# Given a list of numbers:
# [5, 10, 15, 20, 25, 30]
# Perform the following in a single pipeline:
# • Use map() to square each number
# • Use filter() to keep only numbers divisible by 5
# • Use reduce() to calculate the sum of remaining numbers
from functools import reduce
l=[5,10,15,20,25,30]
k=reduce(lambda x,y:x+y,
         list(filter(lambda x: x if x%5==0 else "",
                     list(map(lambda x:x**2,l)))))
print(k)

