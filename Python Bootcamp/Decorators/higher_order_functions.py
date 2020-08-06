from random import choice
#We can nest functions inside one another 

def greet(person):
    def get_mood():
        msg = choice(('Hello there ','Go away ','I love you '))
        return msg

    result = get_mood() + person
    return result

print(greet("Toby"))


def make_laugh_func():
    def get_laugh():
        l = choice(('HAHAHAHA', 'LOL', 'tehehehe'))
        return l

    return get_laugh

laugh = make_laugh_func()
print(laugh())

def make_laugh_at_func(person):
    def get_laugh():
        laugh = choice(('HAHAHA', 'LOL', 'tehehehe'))
        return f"{laugh} {person}"

    return get_laugh

laugh_at = make_laugh_at_func("Linda")
print(laugh_at())
print(laugh_at())
print(laugh_at())
print(laugh_at())
