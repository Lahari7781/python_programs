# def multiplier(x):
#     def inner(y):
#         return x*y
#     return inner
# res=multiplier(3)
# print(res(20))
let=[(1,'banana'),(2,'apple'),(3,'cherry')]
let.sort(key=lambda let:let[1])
print(let)