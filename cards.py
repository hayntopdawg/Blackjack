__author__ = 'FujNasty'

#from card import Card
from random import randint

class Card(object):
    rank_name = (None, "Ace", "2", "3", "4", "5", "6", "7",
            "8", "9", "10", "Jack", "Queen", "King")
    suit_name = ("Spades", "Hearts", "Clubs", "Diamonds")

    def __init__(self, rank = 1, suit = 0):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return "%s of %s" % (Card.rank_name[self.rank], Card.suit_name[self.suit])

# # -----------
# # User Instructions
# #
# # Modify the card_ranks() function so that cards with
# # rank of ten, jack, queen, king, or ace (T, J, Q, K, A)
# # are handled correctly. Do this by mapping 'T' to 10,
# # 'J' to 11, etc...
#
# def card_ranks(cards):
#     "Return a list of the ranks, sorted with higher first."
#     ranks = ['--23456789TJQKA'.index(r) for r,s in cards]
#     ranks.sort(reverse=True)
#     return ranks
#
# print card_ranks(['AC', '3D', '4S', 'KH']) #should output [14, 13, 4, 3]

class Deck(object):
    def __init__(self):
        # deck = []
        # for s in range(4):
        #     for r in range(1, 14):
        #         deck.append(Card(r, s))
        self.deck = self.create_deck()

    def create_deck(self):
        deck = []
        for s in range(4):
            for r in range(1, 14):
                deck.append(Card(r, s))
        return deck

    def shuffle(self):
        """Shuffles the deck with the Fisher-Yates shuffle"""
        num_cards = len(self.deck)
        for i in range(num_cards):
            j = randint(i, num_cards - 1)
            self.deck[i], self.deck[j] = self.deck[j], self.deck[i]