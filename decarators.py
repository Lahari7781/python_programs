def login(fun):
    def inner():
        us=input("Username:")
        ps=input("Password:")
        if us=="lahari07" and ps=="12345":
            return fun()
        else:
            return "Invalid credentials"
    return inner
@login
def file():
    return "Secure File"
print(file())