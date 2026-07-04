def run_twice(func,value):
    value=func(value)
    value=func(value)
    return value
def add(a):
    return a+2
print(run_twice(add,3))