# DEFAULT + KEYWORD + LAMBDA: Write a function make_greeting(name, prefix='Hello', formatter=lambda x: x) that applies formatter to the final greeting string.
# Test with str.upper as the formatter.
def make_greet(name,prefix="Hello",formatter=lambda x:x):
    greeting= f"{prefix},{name}"
    return formatter(greeting)
print(make_greet("Lahari","Hii",str.upper))