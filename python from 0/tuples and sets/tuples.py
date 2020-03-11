#tuple (ordered and immutable)
#using tuple as keys
locations ={
    (35.6895,39.4567): "Tokyo Office",
    (40.8748,98.0292): "New York Office",
    (37.7749,122.098): "San Francisco Office"
}

#accessing a key`s value
print(locations[35.6895,39.4567])
print(locations.items())

#tuple looping and methods
months = ('January','February','March')
for month in months:
    print(month)
i = len(months) - 1

#ao contrario
while i>=0:
    print(months[i])
    i-=1

#count method
x = (1,2,3,4,5)
print(x.count(1))

#index method
t = (1,2,3,3,3)
print(x.index(1))