# # # # # # Write a program to remove a specific element from a list.
# # # # # l=[1,2,3,4,5]
# # # # # l.remove(5)
# # # # # print(l)
# # # # # # Write a program to remove an element from a list using its index.
# # # # # l.pop(2)
# # # # # print(l)
# # # # # # Write a program to find the index of a given element in a list.
# # # # # print(l.index(2))
# # # # # # Write a program to count the number of occurrences of an element in a list.
# # # k=[1,1,2,3,4,1,2,5,7,8,4,6,3,0,2,1,5,6,4]
# # # # # k.count(1)
# # # # # print(k)
# # # # # print(k.count(4))
# # # # # # Write a program to find the sum of the first and last elements of a list
# # # # # s=k[0]+k[len(k)-1]
# # # # # print(s)
# # # # # # Write a program to calculate the sum of list elements up to a given index.
# # # # # n=int(input())
# # # # # s=0
# # # # # for i in range(n):
# # # # #     s=k[i]+s
# # # # # print(s)
# # # # Write a program to calculate the average of odd numbers in a list.
# # # s=c=0
# # # for i in k:
# # #     if(i%2!=0):
# # #         s+=i
# # #         c+=1
# # # print(s//c)
# # Write a program to print all prime numbers present in a list.
# l=[2,5,7,8,9,13,10,15]
# # for i in l:
# #     fc=True
# #     for k in range(2,int(i**0.5)+1):
# #         if(i%k==0):
# #             fc=False
# #     if(fc):
# #         print(i)
# . Write a program to print the next prime number for each element in the list
l=[2,5,7,8,9,13,10,15]
for i in range(len(l)):
    fc=True
    for k in range(2,int(l[i]**0.5)+1):
        if(l[i]%k==0):
            fc=False
    if(fc):
        while True:
            a = l[i] + 1
            c=True
            for p in range(2,int(a**0.5)+1):
                if(a%p==0):
                    c=False
            if(c):
                print(a)
                break
        fc=False





