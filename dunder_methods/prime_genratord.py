def prime(x):
    for i in range(x):
        for j in range(2,int(x**0.5)+1):
            if(i%j==0):
                fc+=1

l=prime(100)
