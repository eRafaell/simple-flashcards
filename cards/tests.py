from django.test import TestCase
from .models import Deck, Card


class CardTestCase(TestCase):
    deck = None
    card1 = None
    card2 = None
    card3 = None

    def setUp(self):
        self.deck = Deck.objects.create(title='test_deck_1')
        self.card1 = Card.objects.create(
            parent_deck=self.deck,
            front='front of card 1',
            back='back of card 1'
        )
        self.card2 = Card.objects.create(
            parent_deck=self.deck,
            front='front of card 2',
            back='back of card 2'
        )
        self.card3 = Card.objects.create(
            parent_deck=self.deck,
            front='front of card 3',
            back='back of card 3'
        )

    def test_starting_conditions(self):
        '''
        check if the deck and cards exists
        '''
        self.assertIsInstance(self.deck, Deck)
        self.assertIsInstance(self.card1, Card)
        self.assertIsInstance(self.card2, Card)
        self.assertIsInstance(self.card3, Card)

    def test_card_has_previous(self):
        '''
        The first card does not have a previous card. All other cards do.
        '''
        self.assertFalse(self.card1.has_previous_card())
        self.assertTrue(self.card2.has_previous_card())
        self.assertTrue(self.card3.has_previous_card())


    def test_get_previous_card(self):
        '''
        The first card should return None. All others should return the previous card in the deck
        '''
        self.assertIsNone(self.card1.get_previous_card())
        self.assertEqual(self.card1, self.card2.get_previous_card())
        self.assertEqual(self.card2, self.card3.get_previous_card())

    def test_card_has_next(self):
        '''
        The last card does not have a next card. All other cards do.
        '''
        self.assertTrue(self.card1.has_next_card())
        self.assertTrue(self.card2.has_next_card())
        self.assertFalse(self.card3.has_next_card())

    def test_get_next_card(self):
        '''
        The last card should return None. All others should return the previous card in the deck
        '''
        self.assertIsNone(self.card3.get_next_card())
        self.assertEqual(self.card3, self.card2.get_next_card())
        self.assertEqual(self.card2, self.card1.get_next_card())



