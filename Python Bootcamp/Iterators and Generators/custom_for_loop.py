'''para entender como funciona por baixo dos panos.'''

def my_for(iterable):
    iterator = iter(iterable)
    while True:
        try:
            print(next(iterator))
        except StopIteration:
            print("End of iterator!")
            break


my_for("hello")