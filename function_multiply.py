def multiply(x):
    def inner(y):
        return (x*y)
    return inner
k=multiply(25)
print(k(30))
l=multiply(70)
print(l(20))