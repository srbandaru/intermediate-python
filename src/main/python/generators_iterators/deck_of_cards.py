from collections import namedtuple

card = namedtuple('Card', ['rank', 'suit'])


class DeckOfCards():
    ranks = list(list(range(2, 11)) + list('JQKA'))
    suits = ['spade', 'clubs', 'diamonds', 'hearts']

    def __init__(self):
        self._cards = [card(rank, suit) for rank in self.ranks for suit in self.suits]

    def __str__(self):
        time_to_print = [str(x.rank) + ' of ' + str(x.suit) for x in self._cards]
        print('Total cards in the deck are {}'.format(len(self._cards)))
        return str('\n'.join(time_to_print))

    def __iter__(self):
        iter(self._cards)


deck = DeckOfCards()

print(deck)
