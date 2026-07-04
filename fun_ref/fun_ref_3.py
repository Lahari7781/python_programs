def up(a):
    return a.upper()
def lo(a):
    return a.lower()
def ti(a):
    return a.title()
dict1={
    "upper":up,
    "lower":lo,
    "title":ti
}
s=input("ENTER UPPER/LOWER/TITLE:")
print(dict1[s]("HELLO"))
