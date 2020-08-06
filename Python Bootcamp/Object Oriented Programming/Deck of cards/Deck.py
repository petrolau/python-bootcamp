from random import shuffle
from Card import Card
class Deck:
    def __init__(self):
        #"Hearts","Diamonds","Clubs","Spades"
        suits = ["Hearts","Diamonds","Clubs","Spades"]
        values = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
        #lista que vai conter a combinacão de todos os suits e values.
        self.cards = [Card(value, suit) for suit in suits for value in values]

    def __repr__(self):
        return f"Deck of {self.count()} cards."
    
    #retorna o número de cartas no deque.
    def count(self):
        return len(self.cards)
    
    #funcão que remove as num cartas desejadas do deque.
    def _deal(self, num):
        #pegando o número de cartas no deque.
        count = self.count()
        #achar o menor número entre count e num, evitando que o jogador 
        #remova mais cartas que as existentes.
        #ex -> remover 5 cartas de 3, remove as 3.
        actual = min([count, num])
        if count == 0:
            raise ValueError ("Todas as cartas foram removidas.")
        #ex [1,2,3,4,5,6]
        cards = self.cards[-actual:] #cards removidas = [4,5,6]
        self.cards = self.cards[:-actual] #cards restantes = [1,2,3]
        return cards
    
    def deal_card(self):
        #tirando uma carta do deque
        return self._deal(1)[0]

    def deal_hand(self, hand_size):
        return self._deal(hand_size)

    def shuffle_cards(self):
        if self.count() < 52:
            raise ValueError("Only full decks can be shuffled!")
        shuffle(self.cards)
        return self
        

d = Deck()
d.shuffle_cards()
hand = d.deal_card()
print(Card)
hand = d.deal_hand(5)
print(hand)