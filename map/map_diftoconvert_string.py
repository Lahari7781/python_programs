# 9. Explain the difference between:
# map(str, [1, 2, 3])
# map(lambda x: str(x), [1, 2, 3])
# Which one is faster and why?
k=list(map(str,[1,2,3]))
print(k)
res=list(map(lambda x:str(x),[1,2,3]))
print(res)