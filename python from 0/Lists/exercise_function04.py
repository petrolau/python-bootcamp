#botando num dicionario quantas vezes cada letra aparece na palavra
def multiple_letter_count(string):
    return {letter: string.count(letter) for letter in string}

print(multiple_letter_count("hello"))