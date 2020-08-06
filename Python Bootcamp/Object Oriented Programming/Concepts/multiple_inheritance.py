class Aquatic:
    def __init__(self,name):
        print("Aquatic init!")
        self.name = name

    def swim(self):
        return f"{self.name} is swimming!"
    
    def greet(self):
        return f"I am {self.name} of the sea! "



class Ambulatory:
    def __init__(self,name):
        print("Ambulatory init!")
        self.name = name
    
    def walk(self):
        return f"{self.name} is walking"

    def greet(self):
        return f"I am {self.name} of the land! "


class Penguim(Ambulatory, Aquatic):
    def__init__(self,name):
        print("Penguim init!")
        Ambulatory.__init__(self, name=name)
        Aquatic.__init__(self, name=name)


jaws = Aquatic("Jaws")
lassie = Ambulatory("Lassie")
captain_cook = Penguim("Captain Cook")