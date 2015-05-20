__author__ = 'FujNasty'

from cards import Card

class Hand(object):
    def __init__(self):
        self.hand = []

    def __str__(self):
        return ','.join([card for card in self.hand])

    def add_card(self, card):
        self.hand.append(card)

    def get_hand_value(self):
        value = 0
        ace = False
        for card in self.hand:
            value += card.get_card_value()
            if card.rank == "Ace":
                ace = True
        if ace and value <= 11:
            value += 10
        return value

class Player(Hand):
    pass

class Dealer(Hand):
    def get_first_card_value(self):
        return self.hand[0].get_card_value()