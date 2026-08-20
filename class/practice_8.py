# Q8. Create a class Course with:
# class variable total_students
# instance variable student_name
# instance method enroll() → increments total_students
# class method show_total(cls) → prints total students
# static method is_eligible(age) → returns True if age ≥ 18
# Demonstrate enrolling multiple students and show total count
class Course:
    total_students=0
    def __init__(self,n):
        self.student_name=n
    def enroll(self):
        Course.total_students+=1
    @classmethod
    def show_total(cls):
        print(cls.total_students)
    @staticmethod
    def is_eligible(age):
        return age>=18
s1=Course("Tamanah")
s1.enroll()
s2=Course("Prabhas")
s2.enroll()
s3=Course("Anushka")
s3.enroll()
s4=Course("Rajamoli")
s4.enroll()
s5=Course("Rana")
s5.enroll()
Course.show_total()
print(Course.is_eligible(20))
print(Course.is_eligible(16))