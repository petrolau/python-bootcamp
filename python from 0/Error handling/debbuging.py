#import pdb 
#first = "First"
#second = "Second"
#pdb.set_trace()
#result = first + second
#third = "Third"
#result += third
#print(result)

def add_numbers(a, b, c, d):
    import pdb; pdb.set_trace()

    return a + b + c + d
add_numbers(1,2,3,4)

#import pdb
#pdb.set_trace()

#também é comum em apenas uma linha:
#import pdb; pdb.set_trace()

#Common PDB commands:
#l (list)
#n (next line)
#p (print)
#c (continue - finishes debugging)