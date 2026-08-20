# # Use a lambda with .sort() to sort this list of tuples by the second element:
# # [(1,'banana'),(2,'apple'),(3,'cherry')]
# # l=[(1,'banana'),(2,'apple'),(3,'cherry')]
# # l.sort(key=lambda x:x[1])
# # print(l)
# s="Hello who?"
# vowels="aeiou"
# k=list(filter(lambda x:x  in vowels ,s))
# p="".join(k)
# print(p)
# Chain map() and filter(): from [1..10], first filter out odds, then square the remaining evens.
l=[1,2,3,4,5,6,7,8,9,10]
m=list(map(lambda x:x**2,list(filter(lambda x:x%2==1,l))))
print(m)