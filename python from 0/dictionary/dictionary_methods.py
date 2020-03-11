#clear -> clears all the keys and values
d = {
    "a" : 1,
    "b" : 2,
    "c" : 3
}
print(d)
d.clear()
print(d)

#copy -> makes a copy of the dictionary
dictionary = {
    "a":1,
    "b":2,
    "c":3
}

clone = dictionary.copy()
print(clone)

#fromkeys --> creating default values
new_user = {}.fromkeys(['name','score','email','profile bio'], 'unknown')
print(new_user)

#get ->retrieves a key in an object and return none if the keys doesnt exist
result = dictionary.get('a')
print(result)
result = dictionary.get('e')
print(result)

'''
pop -> takes a single argument corresponding to a key and removes
that key-value pair from the dictionary. Returns the value 
corresponding to the key that was removed.
'''
dictionary.pop('a')
print(dictionary)

#update -> update keys and values in a dictionary
instructor = {
    "name":"Colt",
    "num_courses":4,
    "favorite_language":"Python "
}
person = {
    "city":"Antigua",
}
person.update(instructor)
print(person)
person['name'] = "Evelia"
print(person)
