# Use map() on a string to convert each character into its ASCII value
# (using ord()). Print the result list.
s="Hello"
k=list(s)
res=list(map(ord,k))
print(res)