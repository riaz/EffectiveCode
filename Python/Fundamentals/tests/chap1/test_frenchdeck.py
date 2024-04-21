from fluentpy.chap1.frenchdeck import FrenchDeck, Card


def test_frenchdeck():
    """
    We will just intantiate the french deck and see if the getter and setter functions are working appropriately
    """
    deck = FrenchDeck()

    assert len(deck) ==  52

    card = Card('A', suit='hearts')

    assert card in deck

    # A hearts will be the last card
    assert Card('A', 'hearts') == deck[-1]

    # 2 spade is the first card
    assert Card('2', 'spade') == deck[0]

    # sorting the deck
    deck = sorted(deck, key=deck.get_rank)

    assert deck[0] == Card('2', 'club')