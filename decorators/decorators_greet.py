def my_decorator(func):
    def inner(name):
        print("Function Starts")
        func(name)
        print("Function ends")
    return inner
@my_decorator
def greet(name):
    print(f"Hello! {name}")
greet("Lahari")