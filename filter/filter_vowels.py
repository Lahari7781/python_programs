# 6. Use filter() to remove all vowels from a string and print the final string.
s="Hey,How are you?"
k=list(filter(lambda x:x not in "AEIOUaeiou",s))
print(k)