def count_up_to(max):
    count = 1
    while count <= max:
        #instead of return, gives a generator object
        yield count
        count += 1

count_up_to(5)
counter = count_up_to(5) 
next(counter)