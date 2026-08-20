# map() + filter() + lambda: Given a list of integers from 1 to 20, use filter() to keep multiples of 3,
# then use map() to square them. Print the result.
k=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
res=list(map(lambda x:x**2,list(filter(lambda x:x%3==0,k))))
print(res)