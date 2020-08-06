list1 = ["CA","NJ","RI"]
list2 = ["California","New Jersey","Rhode Island"]
diction = {list1[i]:list2[i] for i in range (0,3)}
print(diction)

#method zip.
#(key,value)
print(dict(zip(list1,list2)))

#transformando a lista num dicionario
person = [["name","Jared"],["job","Musician"],["city","Bern"]]
answer = {person[i][0]:person[i][1] for i in range (0,3)}
print(answer)
#outro metodo
answer2 = {k:v for k,v in person}
print(answer2)

#vogais chaves e valores iguais a 0
vowels = ['a','e','i','o','u']
dict3 = {vowels[i]:0 for i in range (0,5)}
print(dict3)
#metodo mais simples
dict3_2 = {char:0 for char in 'aeiou'}
print(dict3_2)
#ouuu
dict3_3 = dict.fromkeys("aeiou",0)


#ASCII codes dictionary
#function char -> dando o codigo ASCII ele retorna a string.
# A = 65 , Z = 90

dict4 = {count:chr(count) for count in range(65,91)}
print(dict4)

