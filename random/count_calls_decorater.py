def count_calls(func):
    def inner():
        func()
        global count
        count[0] = count[0] + 1
        print(count)
    return inner
count=[0]
@count_calls
def fun():
    pass
fun()
fun()
fun()


