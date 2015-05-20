from unittest import TestCase

__author__ = 'FujNasty'


class TestHand(TestCase):
    def test_get_hand_value_aces(self):
        from players import Hand
        from cards import Card
        test_hand = Hand()
        test_hand.add_card(Card("9", "Spades"))
        test_hand.add_card(Card("Ace", "Spades"))
        self.assertEquals(test_hand.get_hand_value(), 20)
        test_hand.add_card(Card("Ace", "Hearts"))
        self.assertEquals(test_hand.get_hand_value(), 21)
        test_hand.add_card(Card("Ace", "Clubs"))
        self.assertEquals(test_hand.get_hand_value(), 12)