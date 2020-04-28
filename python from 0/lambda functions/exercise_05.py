#usando map, pegar apenas os numeros divisiveis por 4 em uma lista e retornar uma nova
#lista com os números triplicados.

def triple_and_filter(nums):
    return list(filter(lambda x: x % 4 == 0, map(lambda x: x*3, nums)))

#x for x in nums 
#primeiramente filtra os divisiveis por 4, depois mapeia os numeros e 
#multiplica-os por 3.
#filter(arg1,arg2)
#map(arg1,arg2)