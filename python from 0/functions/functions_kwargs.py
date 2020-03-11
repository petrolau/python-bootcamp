#**kwargs

#coloca os argumentos em um dicionario.

def fav_colors(**kwargs):
    #looping no dicionario chave,valor
    for person,color in kwargs.items():
        print(f"{person}'s favorite color is {color}")


fav_colors(laura="purple",gabriel = "purple")

def special_greeting(**kwargs):
    if "David" in kwargs and kwargs["David"] == "special":
        return "You get a special greeting David!"
    elif "David" in kwargs:
        return f"{kwargs['David']} David!"
    return f"Not sure who this is. . ."

print(special_greeting(David="special", Heather = "Hello"))
