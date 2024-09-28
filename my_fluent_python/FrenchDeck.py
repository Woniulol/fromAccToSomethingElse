import collections
from random import choice

Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self) -> None:
        self._card = [Card(rank, suit) for rank in self.ranks for suit in self.suits]

    def __len__(self) -> int:
        return len(self._card)

    def __getitem__(self, position):
        return self._card[position]

    # if __contains__ is not implemented, in operator will do a O(n) scan
    def __contains__(self, value):
        return value in self._card


if __name__ == "__main__":
    beer_card = Card('7', 'diamonds')
    print(beer_card)

    deck = FrenchDeck()
    print(len(deck))
    print(deck[0])
    print(deck[1])

    print(choice(deck))

    print(deck[:10:2])

    print((Card('Q', 'hearts') in deck))

    print(FrenchDeck.ranks.index(beer_card.rank))






