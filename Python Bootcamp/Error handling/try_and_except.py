#pedaco de código que vai ser tentado (sem quebrar o código)
try:
    laura #var não atribuida/declarada

#caso tenha um erro no try acima, será executado o bloco except.
except:
    print("PROBLEM!")
print("after the try")



#checar se a chave está no dicionário.
def get(d,key):
    try:
        return d[key]
    except KeyError:
        return None
d = {"name": "Colt"}
print(get(d,"name"))  