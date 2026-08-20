import functools
def wrapperfunc(func):
    @functools.wraps(func)
    def inner():
        print(inner.__name__)
        func()
    return inner
@wrapperfunc
def owl():
    print("Hello")
print(owl.__name__)
owl()