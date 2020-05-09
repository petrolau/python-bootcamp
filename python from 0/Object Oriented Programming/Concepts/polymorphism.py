#a mesma operacao funciona diferentemente dependendo do objeto
class Animal():
    #definimos apenas o header da funcao
    def speak(self):
        raise NotImplementedError("Subclass needs to implement this method")


class Dog(Animal):
    def speak(self):
        return "woof"

class Cat(Animal):
    def speak(self):
        return "meow"

Cat= Cat()
print(Cat.speak())