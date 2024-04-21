import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spade club diamonds hearts'.split()

    def __init__(self):
        self._cards = [ Card(rank, suit) for suit in self.suits for rank in self.ranks]
    
    def __len__(self):
        return len(self._cards)

    def __getitem__(self, pos: int) -> Card:
        return self._cards[pos]
    
    def __str__(self) -> str:
        out = []
        for card in self._cards:
            out.append(f"Card : suit {card.suit} rank {card.rank}")
        return "\n".join(out)
    
    def __repr__(self) -> str:
        out = []
        for card in self._cards:
            out.append("Card : suit {0:card.suit!r} rank {0:card.rank!r}".format(card))
        return "\n".join(out)        
    
    def get_rank(self, card) -> int:
        suit_values = dict(spade=3, hearts=2, diamonds=1, club=0)
        rank_value = FrenchDeck.ranks.index(card.rank)
        return rank_value * len(suit_values) + suit_values[card.suit]