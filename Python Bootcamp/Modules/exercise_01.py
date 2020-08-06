#saber se algum argumento passado é uma keyword do python.
import keyword

def contains_keyword(*strs):
    for item in strs:
        if keyword.iskeyword(item):
            return True
    return False

print(contains_keyword("def","return"))
