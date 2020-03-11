#comando add e remove
#locacao end ou beginning
#remove end --> remove o ultimo valor da lista e retorna-o
#remove beginning --> remove o primeiro valor da lista e retorna-o
# add beginning --> adiciona um valor no inicio da lista
# add end --> adiciona um valor no final da lista.
def list_manipulation(lista,comando,locacao,valor):
    #remove end [1,2,3] - > [1,2]
    if comando == "remove" and locacao == "end":
        return lista.pop()
    elif comando == "remove" and locacao == "beginning":
        return lista.pop(0)
    elif comando == "add" and locacao == "end":
        lista.append(valor)
        return lista
    elif comando == "add" and locacao == "beginning":
        lista.insert(0,valor)
        return lista
    

print(list_manipulation([1,2,3],"add","beginning",20))




