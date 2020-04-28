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

#type -> retorna o tipo da var
def is_all_strings(lst):
    return all(type(l) == str for l in lst)

is_all_strings(nums)


#sorted -> Funciona para ordenar tuplas também, retornando uma lista.
more_numbers = [6,1,8,2]
print(sorted(more_numbers))
#do maior para o menor reverse = True
print(sorted(more_numbers,reverse=True))



#what if..
users = [
    {'username' : 'samuel', 'tweets': ["I love cake","I love pie"]},
    {'username' : 'katie', 'tweets': ["I love my cat"],"num":10,"color":"teal"},
    {'username' : 'jeff', 'tweets': []},
    {'username' : 'bob123', 'tweets': []},
    {'username' : 'doggo_luvr', 'tweets': ["dogs are the best"]},
    {'username' : 'guitar_gal', 'tweets': []},

]
print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
print(sorted(users,key=lambda user: user['username']))

#what if 2 ...
songs =[
    {"title":"Happy bday","playcount":1},
    {"title":"Survive","playcount":6},
    {"title":"YMCA","playcount":99},
    {"title":"Toxic","playcount":31},

]
print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
print(sorted(songs,key = lambda s: s['playcount'],reverse = True))



#min e max ->
print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
names = ["Arya","Samson","Dora","Tim","Ollivander"]

print(max(names, key = lambda n: len(n)))
print(min(names, key = lambda n: len(n)))
print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
print(min(songs, key = lambda s: s['playcount']))
print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
#printa só o titulo da musica menos tocada, nao o dic todo
print(min(songs,key = lambda s: s['playcount'])['title'])


#reversed -> retorna um iterator reverse.
for char in reversed("hello world"):
    print (char)


for x in reversed(range(0,10)):
    print (x)

#abs() -> retorna o valor absoluto de um número.
print(abs(-5))

#math.fabs() -> converte para um float, e depois da o valor abs.

#sum([],starting point) -> retorna o total de um iterable, da esquerda para a direita.
print(sum([1,2,3],10))

#round() -> retorna o numero aproximado aos ndigitos de precisão.
print(round(1.212121, 2)) # 1.21

#zip() ->
nums1 = [1,2,3,4,5]
nums2 = [6,7,8,9,10]
z = zip(nums1,nums2)

list(z) #[(1, 6), (2, 7), (3, 8), (4, 9), (5, 10)]
dict(z) # {1: 6, ..... }

five_by_two = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)]
list(zip(*five_by_two)) #unzipping
#[(0,1,2,3,4), (1,2,3,4,5)]


#filter() -> recebe uma funcao e uma lista como argumentos
li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61] 
final_list = list(filter(lambda x: (x%2 != 0) , li)) 
print(final_list) 

#lambda with map() ->
# map() with lambda()  
# to get double of a list. 
li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61] 
final_list = list(map(lambda x: x*2 , li)) 
print(final_list) 


