__author__ = 'FujNasty'

from cards import Deck
from players import Player, Dealer

def deal_game():
    deck = Deck()
    deck.shuffle()
    player = Player()
    dealer = Dealer()
    player.add_card(deck.deal())
    dealer.add_card(deck.deal())
    player.add_card(deck.deal())
    dealer.add_card(deck.deal())
    print("Player has a %s and a %s (%d)" % (player.hand[0], player.hand[1], player.get_value()))
    print("Dealer is showing a %s (%d)" % (dealer.hand[0], dealer.get_value_first_card()))

def hit():
    pass

def stand():
    pass

def double_down():
    pass

def split():
    pass

def insurance():
    pass

def surrender():
    pass