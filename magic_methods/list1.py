# Write a program to create a list by taking input
# from the user and print the list
n=int(input("Enter size of list:"))
l=[]
for i in range(n):
    l.append(int(input()))
print(l)