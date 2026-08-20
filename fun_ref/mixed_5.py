double=lambda x:x**2
triple =lambda x:x**3
quadraple=lambda x:x**4
l=[double,triple,quadraple]
def apply_all(funcs,value):
    for i in l:
        value=func(value)
    return value
print(apply_all(funcs,2))


