# Use functools.reduce() with a lambda to
# find the largest number from a given list Dynamically.
from functools import reduce
l = list(map(int, input("Enter numbers separated by space: ").split()))
largest = reduce(lambda x, y: x if x > y else y, l)
print("Largest number:", largest)