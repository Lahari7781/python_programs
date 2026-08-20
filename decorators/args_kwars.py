# Write a decorator called validate_positive that checks all positional arguments passed to a function.
# If any argument is negative, print an error message
# and return None without calling the function. Test it on a function multiply(a, b).
from functools import reduce
def validate_postive(func):
    def inner(*args):
        for i in args:
            if i<0:
                print("error")
                return None
        func(*args)
    return inner
@validate_postive
def multiply(*args):
    print(reduce(lambda x,y:x*y,args))
multiply(11,-2)


