# **kwargs + reduce(): Write a function weighted_average(**scores) where keys are subjects and values are scores.
# Use reduce() to compute the average of all values.
# from functools import reduce
# def weighted_average(**k):
#     res=reduce(lambda x,y:x+y,k.values())
#     return res
# print(weighted_average(
# Maths=21,English=10,science=15))
student = {
    "name": "Lahari",
    "age": 21
}
for i in student:
    print(i)