# Q10. Create a class Student with:
# class variable passing_marks = 40
# instance attributes name, marks
# instance method result() → prints pass/fail using class variable
# class method update_passing_marks(cls, new_marks)
# static method grade_category(marks) → returns "A", "B", "C" based on score ranges
# Use all three in a program that:
# 1.Creates students
# 2.Updates the passing criteria
# 3.Displays grade category and result
class Student:
    passing_marks=40
    def __init__(self,n,m):
        self.name=n
        self.marks=m
    def result(self):
        if(self.marks>=self.passing_marks):
            print(Student.grade_category(self.marks),end=" ")
            print("Pass")
        else:
            print("Fail")
    @classmethod
    def update_passing_marks(cls,new_marks):
        cls.passing_marks=new_marks
    @staticmethod
    def grade_category(marks):
        if(marks>=90):
            return "A"
        elif(60<=marks<90):
            return "B"
        else:
            return "C"
s1=Student("Rajamatha",10)
s1.update_passing_marks(40)
s1.result()