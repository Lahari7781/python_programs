# Q8. Create a HotelRoom class that:
# Keeps a base price per night (shared).
# Each room has room_number, nights_booked, and guest_name.
# Has a method to calculate total bill.
# Allows updating the base price across all rooms.
# Provides a static utility to check if a number of nights is valid (e.g., positive integer only).
# Demonstrate:
# 1.Creating rooms and bookings.
# 2.Changing base price.
# 3.Checking bill updates and validation.
class HotelRoom:
    base_price=1000
    def __init__(self,rn,nb,gn):
        self.room_number=rn
        self.nights_booked=nb
        self.guest_name=gn
    def total(self):
        total=self.nights_booked*self.base_price
        return total
    @classmethod
    def update(cls,nw):
        cls.base_price=nw
    @staticmethod
    def validate(y):
        if y>0:
            return True
        else:
            return False
b1=HotelRoom(404,5,"Kathrine")
print(b1.total())
b1.update(2000)
print(b1.total())
print(HotelRoom.validate(-1))

