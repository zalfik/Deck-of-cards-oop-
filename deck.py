import random

"""
    Class 'Card' to create a single card with rank & suit attribiute
    Clas 'Deck' to create full deck of 52 'Card' objects (13 ranks with 4 suits)

"""
    

# Link suit to symbol; 's' for Spades, 'c' for Clubs, 'h' for Hearts, 'd' for Dimonds.
suits_symbols = {
    's' : chr(9828),
    'c' : chr(9827),
    'h' : chr(9829),
    'd' : chr(9830)
}

# Build names: 2,3,...,10, J (Jack), Q (Queen), K (King), A (Ace)
rank_names = [str(_) for _ in range(2, 11)] + ['J', 'Q', 'K', 'A']


class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    # Show single card with rank and symbol of a suit
    def show(self):
        print('{}{}'.format(self.rank, suits_symbols[self.suit]))


class Deck:
    def __init__(self):
        self.cards = []

    # Create a list of 52 cards ordered from 2♤ to A♦
    def build(self):
        # Clear cards list before building new deck
        self.cards.clear()

        # Create a deck in cards list
        for rank in rank_names:
            for suit in suits_symbols:
                card = Card(rank, suit)
                self.cards.append(card)
        return self
    
    # Randomize cards order within a list
    def shuffle(self):
        random.shuffle(self.cards)
        return self


    # Show full deck
    def show_deck(self):
        for card in self.cards:
            card.show()


    # Get a single card & delete it from the deck
    def get_card(self):
        card = self.cards.pop()
        return card
        



