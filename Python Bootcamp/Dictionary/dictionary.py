#creating a dictionary
thisdict = { 
    "brand":"Ford",
    "model":"Mustang",
    "year": 1964
}
print(thisdict)

#accessing the items of a dictionary
x = thisdict["model"]

#for loop in a dictionary --> printing one by one
#printing the items
for value in thisdict.values():
    print(value)
#printing the keys
for key in thisdict.keys():
    print(key)
#accessing both
for item in thisdict.items():
    print(item)