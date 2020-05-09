#Method Resolution Order

class Mother:
    def eye_color(self):
        return f"Brown eye color"

    def hair_color(self):
        return f"Dark brown hair color"

    def hair_type(self):
        return f"Curly hair type"



class Father:
    def eye_color(self):
        return f"Blue eye color"

    def hair_color(self):
        return f"Blond hair color"

    def hair_type(self):
        return f"Straight hair type"

class Child(Mother,Father):
    pass

Ana = Child()
print(Ana.eye_color())
print(Ana.hair_color())
print(Ana.hair_type())