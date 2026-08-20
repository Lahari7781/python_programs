# 5.Write a generator that yields only vowels from a string.
def vow(s):
    for i in range(len(s)):
        if(s[i] in "AEIOUaeiou"):
            yield s[i]
for i in vow(input()):
    print(i)