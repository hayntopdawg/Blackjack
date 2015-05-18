__author__ = 'FujNasty'

#from card import Card
from random import randint

# Global variables for cards
RANKS = ("Ace", "2", "3", "4", "5", "6", "7",
        "8", "9", "10", "Jack", "Queen", "King")
SUITS = ("Spades", "Hearts", "Clubs", "Diamonds")
VALUES = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10)

class Card(object):
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.value = VALUES[RANKS.index(rank)]

    def __str__(self):
        return "%s of %s" % (self.rank, self.suit)

class Deck(object):
    '''
    Class to create a standard 52-card deck
    '''
    def __init__(self):
        self.deck = self.create_deck()

    def __len__(self):
        return len(self.deck)

    def create_deck(self):
        '''
        Creates a standard 52-card deck
        :return: deck list of card objects
        '''
        deck = []
        for s in SUITS:
            for r in RANKS:
                deck.append(Card(r, s))
        return deck

    def shuffle(self):
        '''
        Shuffles the deck with the Fisher-Yates shuffle
        '''
        num_cards = len(self.deck)
        for i in range(num_cards):
            j = randint(i, num_cards - 1)
            self.deck[i], self.deck[j] = self.deck[j], self.deck[i]

    def deal(self):
        return self.deck.pop()

class Shoe(Deck):
    '''
    Subclass of Deck.
    '''
    def __init__(self, num_decks = 1):
        self.deck = self.create_shoe(num_decks)

    def create_shoe(self, num_decks):
        '''
        Creates shoe with the indicated number of decks
        :param num_decks: int
        :return: shoe list of card objects
        '''
        shoe = []
        for d in range(num_decks):
            shoe.extend(self.create_deck())
        return shoe