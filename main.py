from deck import *
import blackjack

deck = Deck()
deck.build().shuffle()

# card = Card('A','s')
# card.show()
player = []
for i in range (3):
    my_card = tuple(deck.get_card())
    player.append(my_card)
print(player)
print(blackjack.hand_value(player))