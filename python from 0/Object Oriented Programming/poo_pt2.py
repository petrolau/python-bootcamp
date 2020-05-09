class Pet:
    #class atribute
    allowed = ['cat','dog','cockatoo','cockatiel','fish','guinea pig','rat']
    def __init__(self,name,species):
        if species not in Pet.allowed:
            raise ValueError(f"You can't have a {species} pet!")
        self.name = name
        self.species = species

    def set_species(self,species):
        self.species = species
    
cat = Pet("Blue","cat")
dog = Pet("Wyatt","dog")
Pet.allowed.append("pig")
print(Pet.allowed)

