# Sort a list of tuples(name, age) by age in descending
# order using sorted() with a lambda key.
k=[("Lahari",21),("Madhuri",16)]
res=sorted(k,key=lambda x:x[1],reverse=False)
print(res)

