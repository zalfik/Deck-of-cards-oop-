from deck import rank_names


""" Code by 
    https://brilliant.org/wiki/programming-blackjack/
"""


def card_value(card):
    """Returns the integer value of a single card."""
    card = tuple(card)
    rank = card[0]
    if rank in rank_names[0:-4]:
        return int(rank)
    elif rank is 'A':
        return 11
    else:
        return 10

def hand_value(hand):
    """Returns the integer value of a set of cards."""

    # Naively sum up the cards in the deck.
    tmp_value = sum(card_value(_) for _ in hand)
    # Count the number of Aces in the hand.
    num_aces = len([_ for _ in hand if _[0] is 'A'])

    # Aces can count for 1, or 11. If it is possible to bring the value of 
    #the hand under 21 by making 11 -> 1 substitutions, do so.
    while num_aces > 0:

        if tmp_value > 21 and 'A' in rank_names:
            tmp_value -= 10
            num_aces -= 1
        else:
            break

    # Return a string and an integer representing the value of the hand. If 
    # the hand is bust, return 100.
    if tmp_value < 21:
        return [str(tmp_value), tmp_value]
    elif tmp_value == 21:
        return ['Blackjack!', 21]
    else:
        return ['Bust!', 100]

