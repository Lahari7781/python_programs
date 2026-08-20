class Playlist:
    def __init__(self):
        self.p=[]
    def __add__(self,o2):
        if(".mp3" in o2):
            self.p.append(o2)
            return self
        else:
            print(f"{o2},invalid extension")
    def __contains__(self,o2):
        return o2 in self.p


p1=Playlist()
p1+"Fear.mp3"+"Sunflower.mp3"
print(p1.p)
p1+"vikram.ost"
print(p1.p)