# Q6. Design a class Vehicle that:
# Keeps a record of service charge rate common to all vehicles.
# Each vehicle has a model, kilometers_run, and service history.
# Has a function to calculate service charge based on km and rate.
# Provides a method to update the service rate for all vehicles.
# Provides a static tool to check if a vehicle model is eligible for service (not older than 15 years).
# Demonstrate:
# 1.Creating vehicles with different km and models.
# 2.Updating the service rate.
# 3.Showing charges and eligibility checks.
class Vehicle:
    service_rate=10
    def __init__(self,m,kil,his):
        self.model=m
        self.kilometer_run=kil
        self.service_history=his
    def total(self):
        total=self.service_rate*self.kilometer_run
        return total
    @classmethod
    def update(cls,nw):
        cls.service_rate=nw
    @staticmethod
    def validate(age):
        if(age<15):
            return "Not Eligible"
        else:
            return "Eligible"
v1=Vehicle("XYZ",50,10)
print(v1.total())
v1.update(12)
print(Vehicle.service_rate)
print(Vehicle.validate(12))