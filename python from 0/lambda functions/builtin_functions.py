#all -> 
#retorna true se todos os elementos forem truthy ( ou se estiver vazia)

people = ['Charlie', 'Casey', 'Cody','Carly','Cristina']
boo = all([name[0] == 'C' for name in people])
print(boo)

#any -> retorna true se algum dos elementos forem truthy, se estiver
#vazio retorna false.

nums = [2,60,26,18,21]
boo2 = any([num % 2 == 2 for num in nums])
print(boo2)

#vendo se só tem strings na lista
def is_all_strings(lst):
    return all(type(l) == str for l in lst)

is_all_strings()

#sorted ->
