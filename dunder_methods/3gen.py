# 3.Write a generator that yields each character of a string.
def ch(s):
    for i in range(len(s)):
        yield s[i]
for i in ch(input()):
    print(i)