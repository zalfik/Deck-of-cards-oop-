from deck import *
import blackjack

deck = Deck()
deck.build().shuffle().show_deck()
player = Hand()

for _ in range (3):
    my_card = deck.get_card()
    player.add_card(my_card)

player.show_hand()
deck.show_deck()
