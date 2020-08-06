'''
capitalize("tim") # "Tim"
capitalize("matt") # "Matt"
'''

def capitalize(string):
    #slice method [:1] retorna a letra no index 0
    #[1:] retorna o resto da string a partir do index 0
    return string[:1].upper() + string[1:]


print(capitalize("laura"))