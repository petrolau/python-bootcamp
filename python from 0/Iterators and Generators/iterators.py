'''iterator -> um objeto que pode ser iteravel, que retorna data,
um elemento por vez quando next() é chamado.'''

'''iterable -> um objeto que vai retornar um iterator quando iter()
é utilizado.'''

#next function -> next()
name = "Oprah"
'''tornando o nome um iterator'''
it = iter(name)
for i in range (0,len(name)):
    print(next(it)) 

nums = [1,2,3,4,5]
'''para usar o next, eu preciso que o meu objeto seja um iterator,
   e,para isso, transformamos ele com a funcao iter(obj)'''
it1 = iter(nums)
for c in range (0,len(nums)):
    print(next(it1))
