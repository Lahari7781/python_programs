# 4.Write a generator that yields characters of a string in reverse order.
def rev(s):
    for i in range(len(s)-1,-1,-1):
        yield s[i]
for i in rev(input()):
    print(i)