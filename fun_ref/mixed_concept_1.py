def apply_operations(a,b,op):
     return op(a,b)
add=lambda x,y:x+y
sub=lambda x,y:x-y
prod=lambda x,y:x*y
print(apply_operations(10,5,prod))


