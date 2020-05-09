class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    #Retorna a representacão do objeto.
    def __repr__(self):
        return f"{self.value} of {self.suit}"


