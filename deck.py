suits_symbols = {
    'Spades' : chr(9828),
    'Clubs' : chr(9827),
    'Hearts' : chr(9829),
    'Diamonds' : chr(9830)
}


class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit


    def show(self):
        print('{} of {}'.format(self.value, self.suit))


class Deck:
    def __init_(self):
        self.cards = []
        self.build()

    def build(self):
        for value in ['Spades', 'Clubs', 'Hearts', 'Diamonds']: #suits_symbols.values():
            print(value)

deck = Deck()
deck.build


#        [suits_symbols['{symbol}'] for symobol in ['Spades', 'Clubs', 'Hearts', 'Diamonds']]