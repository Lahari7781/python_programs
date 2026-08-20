# ALL CONCEPTS: Write a function calculator(*args, operation='add', **options) that:
# (a) uses *args to collect numbers,
# (b) uses a default 'add' operation,
# (c) supports operations: 'add', 'multiply', 'max', 'min' using a dict of lambda functions,
# (d) if options contains show_steps=True, prints each step of the calculation.
def calculator(*args,operation='add',**options):
    return d[operation](*args)


d={"add":lambda x,y:x+y,
   "mul":lambda x,y:x*y,
   "max":lambda x,y:x if x>y else y,
   "min":lambda x,y:x if x<y else y}
print(calculator(3,5,operation="add",show_steps=True))