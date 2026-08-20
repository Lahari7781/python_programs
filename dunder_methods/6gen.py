# 6.Write a generator that yields only digits present in a string.
def dig(s):
    for i in range(len(s)):
        if(s[i].isdigit()):
            yield s[i]
for i in dig(input()):
    print(i)