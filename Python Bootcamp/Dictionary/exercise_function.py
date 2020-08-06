# Define speak below:
def speak(animal = "dog"):
    noises = {
        "dog": "woof",
        "pig": "oink",
        "duck": "quack",
        "cat": "meow",
        "cockatoo": "AAA"
    }
    #obter o conteudo da chave animal
    noise = noises.get(animal)
    if noise:
        return noise
    return f"?"

print(speak("henlo"))