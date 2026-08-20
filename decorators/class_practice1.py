class car:
    fuel_type="Petrol"
    def __init__(self,make,model,year,price):
        self.make=make
        self.model=model
        self.year=year
        self.price=price
c1=car("India","Swift Zuv+",2020,100000)
c2=car("China","Porshe",1999,500000)
print(c1.__dict__)
print(c2.__dict__)
print(car.fuel_type)

