#1
#def multiply(*args):
#     product=1
#     for i in args:
#         product*=i
#     return product
# k=multiply(1,2,3,4,5)
# print(k)
#2
# def display_tags(**kwargs):
#     for key,value in kwargs.items():
#         print(f"{key}:{value}")
# display_tags(name="Lahari",age="21")
#3
# def describe_person(name,*hobbies):
#     print(name)
#     print(hobbies)
# describe_person("lahari","1","2","3")
# 4
# def f(*args):
#     print(type(args))
# f(1,2,3)
#5
# def create_html_tag(tag,**attributes):
#     for key,value in attributes.items():
#         print(f"<tag {key} = {value}>")
# create_html_tag('a', href="https://python.org", target="_blank")
#6
def mixed(a,b,*args,**kwargs):
    print(a,b,args,kwargs)
mixed(1,2,3,3,3,4,5,x=10,y=20,z=30)








