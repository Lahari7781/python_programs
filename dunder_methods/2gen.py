# 2.Write a generator that yields even numbers from 1 to N
def Even(n):
    for i in range(n):
        if(i%2==0):
            yield i
n=int(input())
for i in Even(n):
    print(i)