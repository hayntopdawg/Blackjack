__author__ = 'FujNasty'

from cards import Deck
from players import Player, Dealer

deck = Deck() # Make global
player = Player() # Make global
dealer = Dealer() # Make global

def deal_game():
    deck.create_deck()
    deck.shuffle()
    player.hand = [] # Create clear hand function
    dealer.hand = [] # Create clear hand function
    player.add_card(deck.deal())
    dealer.add_card(deck.deal())
    player.add_card(deck.deal())
    dealer.add_card(deck.deal())
    print("Player has a %s and a %s (%d)" % (player.hand[0], player.hand[1], player.get_hand_value()))
    print("Dealer is showing a %s (%d)" % (dealer.hand[0], dealer.get_first_card_value()))

def play_game():
    player_choice = ""
    # If dealer is showing a ten, does dealer have 21

        # Dealer wins unless player has 21, which is a push

    # If dealer is showing an Ace

        # If dealer

        # If player has 21 and dealer is showing an Ace ask if player wants even money

    # If player does not have 21 and dealer has an Ace, does player want insurance

    # If player has a pair, does player want to split

    # Does the player hit, double-down, or stand (Input validation required)
    while player_choice != "h" and player_choice != "s" and player_choice != "d":
        player_choice = input("Hit, Double-down, or Stand? (H/D/S): ").lower()

    # If choice was to hit or double-down: deal one card
    if player_choice == "h" or player_choice == "d":
        hit()

        if player_choice == "d":
            player_choice = "s"

    # Check if player busted or has 21

    # While player_choice != stand
    while player_choice != "s":
    # Does the player hit or stand
        player_choice = input("Hit or Stand? (H/S): ").lower()

        # If choice was to hit: deal one card
        if player_choice == "h":
            hit()

        # Check if player busted or has 21

    # While dealer.get_value() < hard 17

    # Check who wins

def hit():
    player.add_card(deck.deal())
    print("Player has %d:" % player.get_hand_value())
    for card in player.hand:
        print(card)

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

def even_money():
    pass

if __name__ == '__main__':
    while True:
        deal_game()
        play_game()
        play = input("Quit? [type q to quit]: ")
        if play == "q":
            break