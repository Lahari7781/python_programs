# Q1. Create a class Student that:
# Keeps track of the total number of students created.
# Determines whether a student passed or failed based on a shared passing mark.
# Provides a method to curve marks by increasing everyone’s marks by a percentage.
# Has a utility to convert marks (0–100) into letter grades (A, B, C, etc.).
# Demonstrate:
# 1.Creating multiple students.
# 2.Applying a grading curve.
# 3.Displaying updated results with letter grades.
class Student:
    total_number=0
    passing_marks=40
    def __init__(self,n,marks):
        self.name=n
        self.marks=marks
        Student.total_number+=1
    def grading_curve(self,percent):
        self.marks = self.marks + (self.marks * percent / 100)
    def result(self):
        if (self.marks >= Student.passing_marks):
            print(f"Passed with ",end="")
            if (self.marks>=90):
                print("A")
            elif (60<=self.marks<=90):
                print("B")
            else:
                print("C")
        else:
            print("Failed")
s1=Student("Rajesh",20)
s1.grading_curve(10)
s1.result()
