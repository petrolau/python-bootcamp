#Sem valores duplicados 
#Nao ordenados

s = {1,4,5}
for thing in s:
    print(thing)

cities = ["Los Angeles","Boulder","Kyoto","Florence","Santiago","Los Angeles","Tokyo","Boulder","Oslo"]
#cidades nao repetidas -> transformando num set.
print(set(cities))

#set methods e set math
s = {1,2,3}
s.add(4)
s.add(4)
print(s)
s.remove(4) #ou discard
print(s)

s2=s.copy()#copiando o set
print(s2)

#set math 
math_students = {"Matthew","Helen","Prashant","James","Aparna"}
biology_students= {"Jane","Matthew","Charllote","Mesut","Oliver","James"}
#set union
students = math_students | biology_students
print(students)
#set intersection
students_same = math_students & biology_students
print(students_same)


