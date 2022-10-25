from urllib import response
from deck import *


""" Blackjack gameplay
"""

#Return the integer value of a single card.
def card_value(card):
    rank = card.rank
    if rank in rank_names[0:-4]:
        return int(rank)
    elif rank == 'A':
        return 11
    else:
        return 10


# Return the integer value of a set of cards
def hand_value(hand):

    # Naively sum up the cards in the deck.
    tmp_value = sum(card_value(_) for _ in hand)
    # Count the number of Aces in the hand.
    num_aces = len([_ for _ in hand if _.rank == 'A'])

    # Aces can count for 1, or 11. If it is possible to bring the value of 
    # the hand under 21 by making 11 -> 1 substitutions, do so.
    while num_aces > 0:
        if tmp_value > 21:
            tmp_value -= 10
            num_aces -= 1
        else:
            break

    # Return a string and an integer representing the value of the hand. If 
    # the hand is bust, return 0.
    if tmp_value < 21:
        return [str(tmp_value), tmp_value]
    elif tmp_value == 21:
        return ['Blackjack!', 21]
    else:
        return ['Bust!', 100]


# Initialize full gameplay
def start_game():

    # Setup a new deck for a game
    deck = Deck()
    deck.build().shuffle()
    #deck.show_deck()

    dealer = Hand()
    dealer.add_card(deck.get_card())
    #dealer.show_hand()

    player = Hand()
    player.add_card(deck.get_card()).add_card(deck.get_card())
    #player.show_hand()

    #deck.show_deck()

    print(f'Dealers first card:', end=' ')
    dealer.cards[0].show()


    player_in = True
    while player_in:


        game_hand_value = hand_value(player.cards)[1]
        if game_hand_value == 100:
            print('Busted, dealer wins \n with hand:', end=' ')
            player.show_hand()
            break
        elif game_hand_value == 21:
            print('Blackjack! You win! \n your hand:', end=' ')
            player.show_hand()
            break
        else:
            print(f'\nCurrent score:{game_hand_value} \n with hand:', end=' ')
            player.show_hand()

        response = int(input('Hit or stay? (Hit=1, Stay=0) '))

        if response:
            new_card = deck.get_card()
            player.add_card(new_card)
        else:
            player_in = False

    dealer_hand_value = hand_value(dealer.cards)[1]
    if game_hand_value < 21:
        while dealer_hand_value < 17:
            dealer.add_card(deck.get_card())
            dealer_hand_value = hand_value(dealer.cards)[1]
            print(f'\nCurrent dealer score:{dealer_hand_value} \n with hand:', end=' ')
            dealer.show_hand()    
        if (dealer_hand_value == 100) or (game_hand_value > dealer_hand_value):
            print('\nYou win!')
        else:
            print('\nYou loose!')