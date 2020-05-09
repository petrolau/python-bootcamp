#exemplo simples 01
class Animal:

    def make_sound(self,sound):
        print(f"this animal says {sound}")

#passando a classe pai como argumento da classe filha.
class Cat(Animal):
    pass 

blue = Cat()
blue.make_sound("MEOW")


################################################################
#Propriedades
class Human:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        if age >=0:
            #_age =  atributo privado! 
            self._age = age
        else:
            self._age = 0

    #impedindo que alguém coloque uma idade negativa.
    # def get_age(self):
    #   return self._age

    # def set_age(self,new_age):
    #    if new_age >= 0:
    #        self._age = new_age
    #    else:
    #        self._age = 0

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value >=0:
            self._age = value
        else:
            raise ValueError("Age can't be negative")

    @property
    def full_name(self):
        return f"{self.first} {self.last}"

    @full_name.setter
    def full_name(self, name):
        self.first, self.last = name.split(" ")


jane = Human("Jane","Goodall",20)
print(jane.age)
jane.age = 300
print(jane.age)
jane.full_name = "Tim Minchin"
print(jane.full_name)
