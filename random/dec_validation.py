def register(func):
    k=[]
    def inner(a:str,b:str,c:int):
        nonlocal k
        if a in k:
            print("UserName already exist")
        else:
            print("Username Accepted")
            sp = ['@', '*', '!', '#', '$', '%', '&', '_', '-', '=', '+', '/']
            if len(b) >= 8:
                up = list(filter(lambda x: x.isupper(), b))
                sc = list(filter(lambda x: x in sp, b))
                dg = list(filter(lambda x: x.isdigit(), b))
                if up and sc and dg :
                    print("Strong Password")
                    if (c < 18):
                        print("Age is Not Accepted as it is  less than 18")
                    else:
                        print("Age is Accepted")
                        k.append(a)
                        func(a,b,c)
                else:
                    print("Weak Password")
            else:
                print("password must contain 8 characters")
    return inner


@register
def registration(us,psd,age):
    print(f"{us} and {psd} and {age} is accepted")
registration("lahari","1242@Abin0",21)
registration("laari","1242Abin0",21)
registration("Madhu","1242Abin0",21)
registration("Madhu","1242Abin0",21)
registration("Sloka","1242Abin0",13)
registration("Slok","1242A@bin0",30)

