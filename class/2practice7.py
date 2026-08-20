# Q7. Build an Inventory class that:
# Tracks the total number of items across all inventories.
# Each instance maintains its own stock dictionary ({"item": quantity}).
# Provides a method to add or remove stock.
# Allows updating a minimum stock threshold globally.
# Offers a static checker to verify if a stock level is below threshold.
# Demonstrate:
# 1.Managing multiple inventories.
# 2.Adjusting stock threshold.
# 3.Using static validation inside the instance logic.
class Inventory:
    total_items=0
    threshold=20
    def __init__(self):
        self.stock={}
    def add_stock(self,item,qty):
        if(self.valid(qty)):
            self.stock[item]=qty
            Inventory.total_items+=1
            self.display()
        else:
            print("qty is invalid")
    def remove(self,item):
        if item in self.stock.keys():
            self.stock.pop(item)
            Inventory.total_items-=1
            self.display()
        else:
            print("item not found")
    @staticmethod
    def valid(qty):
        return qty>=Inventory.threshold
    def display(self):
        for i,j in self.stock.items():
            print(f"{i}:{j}")
        print(f"minimum threshold:{self.threshold}")
    @classmethod
    def update(cls,nw):
        cls.threshold=nw
i1 = Inventory()
i2 = Inventory()
print("Inventory 1:")
i1.add_stock("Laptop", 30)
i1.add_stock("Mouse", 25)
print("\nInventory 2:")
i2.add_stock("Keyboard", 40)
i2.add_stock("Monitor", 10)   # invalid because 10 < 20
print("\nTotal items:", Inventory.total_items)
# 2. Adjusting stock threshold
Inventory.update(10)
print("\nNew threshold:", Inventory.threshold)
# 3. Static validation inside instance logic
i2.add_stock("Monitor", 15)   # now valid because threshold is 10
# Removing stock
print("\nAfter removing Mouse:")
i1.remove("Mouse")
print("\nTotal items:", Inventory.total_items)

