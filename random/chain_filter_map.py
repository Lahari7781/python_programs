# Chain map() and filter(): from [1..10], first filter out odds, then square the remaining
# evens.
k=[1,2,3,4,5,6,7,8,9,10]
res=list(map(lambda x:x**2,list(filter(lambda x: x%2==0,k))))
print(res)
