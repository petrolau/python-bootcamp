#list comprehension
def intersection(lista1,lista2):
    lista3 = [valor for valor in lista1 if valor in lista2]
    return lista3

print(intersection([1,2,3],[3,4,5]))

#withou list comprehension
def intersection(l1, l2):
    in_common = []
    for val in l1:
        if val in l2:
            in_common.append(val)
    return in_common