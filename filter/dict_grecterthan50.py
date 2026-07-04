# Given a dictionary: d = {"apple": 100, "banana": 40, "cherry": 150} . Use filter() to keep only the keys whose values are greater than 50.
d={"apple":100,"banana":40,"cherry":150}
k=list(filter(lambda x:d[x]>50,d))
print(k)