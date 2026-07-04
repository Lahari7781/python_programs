def multiplier(x):
    def inner(y):
        return x*y
    return inner
res=multiplier(3)
print(res(20))
