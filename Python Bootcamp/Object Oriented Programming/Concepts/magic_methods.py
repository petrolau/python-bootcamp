from copy import copy
class Human:
    def __init__(self,first,last,age):
        self.first = first
        self.last = last
        self.age = age

    def __repr__(self):
        return f"Human named {self.first} {self.last} aged {self.age}"

    def __len__(self):
        return self.age

    def __add__(self, other):
        return Human(first="Newborn",last =self.last, age = 0)

    #n referencias para o MESMO objeto
    #com copy, podemos ter diferentes objetos.  
    def __mul__(self,other):
        #other = int que estiver multiplicando
        return [copy(self) for i in range(other)]

j = Human("Jenny","Larsen",47)
k = Human("Kevin","Jones",49)
print(j)
print(len(j))
print(j+k)
triplets = j*3
triplets[1].first = 'Jessica'
triplets[2].first = 'Chiara'
print(triplets)


