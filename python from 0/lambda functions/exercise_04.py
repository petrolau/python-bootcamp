#Interleaving Strings
#Aqui, vou criar uma funcao que recebe 2 strings e deve junta-las de acordo
#com o seu índice. 

#ex -> interleave('hi','ha') output -> hhia


def interleave(str1, str2):
    return ''.join(''.join(x) for x in (zip(str1,str2)))
#o zip(str1,str2) irá retornar uma lista de tuplas -> [('h','h'),('i','a')]
#agora tenho que transformar essa lista de tuplas em uma string ->
#o join(x) for x in zip(str1,str2) irá retornar ['hn','io']
#o join mais externo irá retornar a string final 'hnio'

print(interleave('hi','ha'))