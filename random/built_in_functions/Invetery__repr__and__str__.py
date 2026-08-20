class Inventory:
    def __init__(self):
        self.items=[]
    def add(self,items:list):
        self.items.extend(items)
    def __str__(self):
        return f"items.{self.items}\n Total:{len(self.items)}"
    def __repr__(self):
        return f"{len(self.items)}"
i1=Inventory()
i2=Inventory()
i3=Inventory()
i1.add(["milk","cake"])
i2.add(["Bread","thum","rice"])
i3.add(["rice","fruits","coke","kiwi"])
print(i1)
l=[i1,i2,i3]
print(l)