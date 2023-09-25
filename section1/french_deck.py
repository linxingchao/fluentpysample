import collections

Card = collections.namedtuple('Card',['rank','suit'])
suit_values = dict(spades=3,diamons=1,hearts=2,clubs=0)

class FrenchDeck:
    ranks = [str(n) for n in range(2,11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()
    
    
    def __init__(self):
        self._cards = [Card(rank,suit) for rank in self.ranks
                                       for suit in self.suits]
        
    def __len__(self):
        return len(self._cards)
    
    def __getitem__(self,position):
        return self._cards[position]

def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]

