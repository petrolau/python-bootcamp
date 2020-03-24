def display_names(first, second):
    print (f"{first} says hello to {second}")

names = {
    "first" : "Laura",
    "second" : "Rusty"
}

display_names(**names)


def add_and_multiply_numbers(a,b,c,**kwargs):
    print(a+b*c)
    print (f"Other stuff...")
    print(kwargs)

data = {
    "a" : 1,
    "b" : 2,
    "c" : 3,
    "name" : "Laura",
    "music" : "kpop"
}
add_and_multiply_numbers(**data)