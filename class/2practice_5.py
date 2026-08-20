# Q5. Create a class Course that:
# Tracks total courses created.
# Each course has a title, duration, and enrolled_students.
# Provides a method to enroll a new student.
# Allows updating the minimum duration for a valid course across all instances.
# Has a static function to check if a given duration is realistic (not negative, not too large).
# Demonstrate:
# 1.Creating multiple courses.
# 2.Enrolling students.
# 3.Updating minimum duration and checking durations.
class Course:
    total=0
    mini_duration=2
    def __init__(self,t,d,e):
        self.title=t
        self.duration=d
        self.enrolled_students=e
        Course.total+=1
    def new_enroll(self,nw):
        self.enrolled_students+=nw
    @staticmethod
    def validate(d):
        if(d>0 and d<=12):
            return True
        else:
            return False
    @classmethod
    def update(cls,nw):
        cls.mini_duration=nw
c1=Course("Python",1,45)
c1.new_enroll(5)
print(c1.enrolled_students)
c1.update(3)
print(Course.mini_duration)
print(Course.validate(0))




