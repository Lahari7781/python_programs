# 9.Create a generator that yields cumulative sum of numbers in a list. Example: [1,2,3] → 1, 3, 6
def sum(l):
    sum=0
    for i in l:
        sum+=i
        yield sum
for i in sum(list(map(int,input("enter numbers:").split()))):
    print(i)