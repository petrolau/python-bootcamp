#map function
nums = [2,4,6,8,10]
doubles = list(map(lambda x: x*2, nums))

print(doubles)


people = ["laura", "dana", "annabel"]
peeps = list(map(lambda name: name.upper(), people))
print(peeps)


names = [
    {'first' : 'Laura', 'last': 'Petrola'},
    {'first' : 'Anna', 'last': 'Unknown'},
    {'first' : 'Elsa', 'last': 'Frozen'}
]

first_names = list(map(lambda x: x['first'],names))
print(first_names)

#Filter function
l = [1,2,3,4]
evens = list(filter(lambda x: x%2 == 0, l))
print(evens)

#colocando os nomes com a em uma lista
l2 = ['austin','andrew','laura']
a_names = list(filter(lambda n: n[0] == 'a',l2 ))
print(a_names)

users = [
    {'username' : 'samuel', 'tweets': ["I love cake","I love pie"]},
    {'username' : 'katie', 'tweets': ["I love my cat"]},
    {'username' : 'jeff', 'tweets': []},
    {'username' : 'bob123', 'tweets': []},
    {'username' : 'doggo_luvr', 'tweets': ["dogs are the best"]},
    {'username' : 'guitar_gal', 'tweets': []},

]

#inactive_users = list(filter(lambda u: len(u['tweets']) == 0, users))
#print(inactive_users)

#Combinando map e filter
inactive_users = list(map(lambda user: user["username"].upper(),
filter(lambda u: len(u['tweets']) == 0, users)))

print(inactive_users)

#e com list comprehension:
inactive_users2 = [user for user in users if not user["tweets"]]
print(inactive_users2)