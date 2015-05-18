__author__ = 'FujNasty'

class Hand(object):
    def __init__(self):
        self.hand = []
        self.value = 0

    def __str__(self):
        return ','.join([card for card in self.hand])

    def add_card(self, card):
        self.hand.append(card)

    def get_value(self):
        ace = False
        for card in self.hand:
            self.value += card.value
            if card.rank == "Ace":
                ace = True
        if ace and self.value <= 10:
            self.value += 10