# 1. Given a list of numbers, create a new list containing only the even numbers using list comprehension.
l=[1,2,3,4,5,6,7,8,9]
m=[i for i in l if i%2==0]
print(m)
# 2. Given a list of numbers, create a list containing the squares of all numbers using list comprehension.
l=[1,2,3,4,5,6,7,8,9]
m=[i*i for i in l]
print(m)
# 3. Given a list of marks, create a new list containing "Pass" if the mark is greater than or equal to 40, otherwise "Fail".
from random import randint
l=[randint(25,100) for i in range(10)]
m=["pass" if i>40 else "fail" for i in l]
#extra create dic with 30:fail
dict={i:j for i,j in zip(l,m)}
print(dict)
# 4. Given a list containing duplicate numbers, create a set containing only the unique even numbers using set comprehension.
num= [10, 15, 10, 20, 25, 20, 30, 35, 30]
s={i for i in num if i%2==0}
print(s)
# 5. Given a list of words, create a set containing the lengths of the words using set comprehension.
w = ["Python", "Java", "C", "Django", "Python"]
s={len(i) for i in w }
print(s)
# 6. Given:
s = {"Rahul": 75,"Anil": 32,"Priya": 56,"Sneha": 28}
#
# 	Create a new dictionary using dictionary comprehension where each student's name is mapped to "Pass" or "Fail".
dict={i:"pass" if j>40 else "fail" for i,j in s.items()}
print(dict)
# 7. Given two lists:
u= ["charan", "rahul", "priya", "sneha"]
p = ["abc123", "xyz456", "pqr789", "hello123"]
#
# 	Create a dictionary where each username is mapped to its corresponding password using dictionary comprehension.
dict={i:j for i,j in zip(u,p)}
print(dict)
# 8. Given:
products = {
     	    "Laptop": 65000,
     	    "Mouse": 500,
     	    "Keyboard": 1500,
     	    "Monitor": 12000
     	    }
#
# 	Create a new dictionary where the value is "Expensive" if the price is greater than 10000, otherwise "Affordable".
dict={i:"Expensive" if j>10000 else "Affordable" for i,j in products.items()}
print(dict)
# 9. Given:
students = {"Rahul": 35,"Anil": 72,"Priya": 81,"Sneha": 29,"Kiran": 65}

# 	Create a new dictionary containing only students who passed, using dictionary comprehension.
dict={i:j for i,j in students.items() if j>40}
print(dict)
# 10. Create a generator expression that generates the squares of numbers from 1 to 10.
gen=(i*i for i in range(1,10))
print(next(gen))
print(next(gen))
print(next(gen))
# 	Use next() to display the first three generated values.
#
# 11. Create a generator expression that generates only even numbers from 1 to 20.
# 	Use a for loop to display the generated values.
gen=(i for i in range(1,20))
for i in gen:
    print(i)
# 12. Given:
n= [10, 15, 20, 25, 30, 35]
# 	Create a generator expression that produces only numbers greater than 20.
gen=(i for i in n if i>20)
for i in gen:
    print(i)
# 13.Student Result System Given:
marks = {"Rahul": 85,"Anil": 32,"Priya": 76,"Sneha": 45,"Kiran": 28}
# Using dictionary comprehension, create a new dictionary where each student's name is mapped to:
#
# "Distinction" if marks are >= 75
# "Pass" if marks are >= 40
# "Fail" otherwise
dict={i:"Destinction" if marks[i]>=75 else "Pass" if marks[i]>=40 else "Fail" for i in marks}
print(dict)
# 14. Given:
usernames = ["admin", "charan", "root", "guest", "developer"]
#
# Create a dictionary using dictionary comprehension where each username is mapped to "Valid" if its length is at least 5, otherwise "Invalid".
dict={i:"Valid" if len(i)>=5 else "Invalid" for i in usernames}
print(dict)
# 15. Given:
names = ["Rahul", "Priya", "Kiran", "Sneha"]
marks = [75, 35, 82, 28]
# Create a dictionary using dictionary comprehension: {"Rahul": "Pass", "Priya": "Fail", "Kiran": "Pass", "Sneha": "Fail"}
# Do not use zip() and do not use a traditional for loop.
dict={names[i]:"Pass" if marks[i]>35 else "fail" for i in range(0,len(names))}
print(dict)