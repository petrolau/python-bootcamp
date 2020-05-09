#primeira letra maiuscula em uma nova lista
names = ["Elie", "Tim", "Matt"]
answer = [name[0] for name in names]
print(answer)

#numeros pares da sequencia em uma nova lista
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = [num for num in numbers if num%2 == 0]
print(even_numbers)

#numeros em comuns das listas em uma nova lista
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
answer2 = [num for num in list1 if num in list2]
print(answer2)

#reversing a string with slice  [::-1]
list3 = ["Ellie", "Tim", "Matt"]
answer3 = [name[::-1].lower() for name in names ]
print(answer3)

#numeros de 1 a 100 divisiveis por 12 em uma nova lista
answer = [num for num in range (1,101) if num%12 == 0]
print(answer)

name = "amazing"
answer4 = [char for char in name if char not in 'a,e,i,o,u']
print(answer4)
