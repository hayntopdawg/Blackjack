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
    print("Player has a %s and a%s (%d)" % (str(player).split(",")[0], str(player).split(",")[1], player.get_hand_value()))
    print("Dealer is showing a %s (%d)" % (str(dealer).split(",")[0], dealer.get_first_card_value()))

def check_dealer_start_hand():
    if dealer.get_hand_value() == 21 and player.get_hand_value() == 21:
        return "push"
    elif dealer.get_hand_value() == 21:
        return "dealer blackjack"
    elif player.get_hand_value() == 21:
        return "blackjack"
    else:
        return ""

def ask_even_money():
    choice = ""
    while choice != "y" and choice != "n":
        choice = input("Even money? (y/n): ").lower()
    return True if choice == "y" else False

def ask_insurance():
    choice = ""
    while choice != "y" and choice != "n":
        choice = input("Insurance? (y/n): ").lower()
    return True if choice == "y" else False

def check_opening_conditions():
    even_money = False
    insurance = False
    outcome = ""

    # If dealer is showing a ten, check for 21
    if dealer.get_first_card_value() == 10:
        outcome = check_dealer_start_hand()

    # If dealer is showing an Ace
    elif dealer.get_first_card_value() == 1:
        # If player has 21 and dealer is showing an Ace ask if player wants even money
        if player.get_hand_value() == 21:
            even_money = ask_even_money()

        # Does player want insurance
        insurance = ask_insurance()

        # Check if dealer has 21
        outcome = check_dealer_start_hand()

    # If player has 21, player has blackjack
    elif player.get_hand_value() == 21:
        outcome = "blackjack"

    return outcome, even_money, insurance

def play_game():
    player_choice = ""

    # Check opening conditions
    outcome, even_money, insurance = check_opening_conditions()

    if outcome == "":
        ################### Player's choices ####################
        # If player has a pair, does player want to split

        # Does the player hit, double-down, or stand (Input validation required)
        while player_choice != "h" and player_choice != "s" and player_choice != "d":
            player_choice = input("Hit, Double-down, or Stand? (h/d/s): ").lower()

        # If choice was to hit or double-down: deal one card
        if player_choice == "h" or player_choice == "d":
            hit()

            if player_choice == "d":
                player_choice = "s"

        # Check if player busted or has 21
        if player.get_hand_value() == 21:
            player_choice = "s"
        elif player.get_hand_value() > 21:
            player_choice = "s"
            outcome = "dealer"

        # While player_choice != stand
        while player_choice != "s":
            # Does the player hit or stand
            player_choice = input("Hit or Stand? (h/s): ").lower()

            # If choice was to hit: deal one card
            if player_choice == "h":
                hit()

            # Check if player busted or has 21
            if player.get_hand_value() == 21:
                player_choice = "s"
            elif player.get_hand_value() > 21:
                player_choice = "s"
                outcome = "dealer"

        ################### Dealer's choices ####################
        # Dealer reveals hidden card

        # While dealer.get_value() < hard 17
        while dealer.get_hand_value() < 17 and outcome != "dealer":
            # Need to account for soft 17
            dealer.add_card(deck.deal())
            print("Dealer hits.")
            print("Dealer has %d:" % dealer.get_hand_value())
            print(dealer)
            if dealer.get_hand_value() > 21:
                outcome = "player"

    ################### Win conditions ####################
    # Check who wins
    if outcome == "blackjack":
        print ("Blackjack!")
        print("Dealer has %d:" % dealer.get_hand_value())
        print(dealer)
    elif outcome == "dealer blackjack":
        print("Sorry, dealer has blackjack. Player loses.")
    elif outcome == "dealer":
        print("Sorry, player busted.")
        print("Dealer has %d:" % dealer.get_hand_value())
        print(dealer)
    elif outcome == "player":
        print("Dealer, busted. Player wins!")
    elif dealer.get_hand_value() > player.get_hand_value():
        print("Sorry, player loses.")
        if len(dealer.hand) == 2:
            print("Dealer has %d:" % dealer.get_hand_value())
            print(dealer)
    elif dealer.get_hand_value() == player.get_hand_value():
        print("Push.")
        if len(dealer.hand) == 2:
            print("Dealer has %d:" % dealer.get_hand_value())
            print(dealer)
    else:
        print("Player wins!")
        if len(dealer.hand) == 2:
            print("Dealer has %d:" % dealer.get_hand_value())
            print(dealer)

def hit():
    player.add_card(deck.deal())
    print("Player has %d:" % player.get_hand_value())
    print(player)

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