l=[20,13,15,30]
k=list(filter(lambda x:x if x%2==0 or x%5==0 else "",l))
print(k)