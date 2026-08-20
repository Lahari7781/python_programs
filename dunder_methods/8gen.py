# 8.Write a generator that yields digits from an integer one by one.
def digi(n):
    k=str(n)
    for i in range(len(k)):
        yield k[i]
for i in digi(int(input())):
    print(i)