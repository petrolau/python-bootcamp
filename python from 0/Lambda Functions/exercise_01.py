#Retornar a maior magnitude de uma lista.

def max_magnitude (nums):
    nums2 = [abs(num) for num in nums]
    return (max(nums2))

lista = [300,20,-900]
max_magnitude(lista)