#somando os valores pares de uma série de inputs.
def sum_even_values(*args):
    return sum(arg for arg in args if arg%2 == 0)

print(sum_even_values(1,2,3,4,5,6))

#somando os valores floats de uma série de inputs. type()
def sum_floats(*args):
    return sum(arg for arg in args if type(arg)  == float)

print(sum_floats(1.5,2.4))