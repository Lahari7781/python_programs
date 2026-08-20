def adding(x:int,y:int) ->int:
    return x+y
print(adding("asd","asdf"))
print(adding.__annotations__)
# here annotation stores type of variables in the function
print(adding.__name__)

def add(x,y):
    return x+y
a=add
