class A:
    def do_something(self):
        print("Method Defined In: A")

class B(A):
    def do_something(self):
        print("Method Defined In: B")

class C(A):
    def do_something(self):
        print("Method Defined In: C")

class D(B,C):
    def do_something(self):
        print("Method Defined In: D")


''' Métodos importantes para descobrir a ordem dos métodos '''
print(D.__mro__) #--> Vai me dar a ordem dos métodos
print(help(D))
#thing = D()
#thing.do_something()

    #   A -->Base class
    #  / \
    # B   C --> B e C herdam de A
    # \   /
    #   D  