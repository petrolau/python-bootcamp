#*args -> posso inputar quantos argumentos eu quiser, serao adicionados
#em uma tupla.

def sum_all_nums(*nums):
    total = 0
    for num in nums:
        total += num
    return total

print(sum_all_nums(1,2,3))