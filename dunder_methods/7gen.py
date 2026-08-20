# 7.Write a generator that yields the square of each element in a list.
def sq(l):
    for i in l:
        yield i*i
for i in sq([1,2,3,4,5]):
    print(i)


