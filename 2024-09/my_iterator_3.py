"""
Dont't make the iterable an iterator itself

Iterables have an `__iter__` method that instantiates a new iterator every time.
Iterators implement an `__next__` method that returns individual items, and an `__iter__` method that returns `self`.

Therefore, iterators are also iterable (because both have `__iter__` method).
But iterable is not iterator.

Iterator pattern requires multiple traversals, which means a proper implementation of the pattern requires each all to `iter(my_iterable)` to create a new,
independent, iterator. That is why we need to split the Sentence iterable to SentenceIterator.
"""

import re
import reprlib

RE_WORD = re.compile(r"\w+")

class WrongSentenceIterableIterator:

    def __init__(self, text) -> None:
        self.index = 0
        self.text = text
        self.words = RE_WORD.findall(text)

    def __repr__(self):
        return f'Sentence({reprlib.repr(self.text)})'

    def __iter__(self):
        return self

    def __next__(self):
        try:
            word = self.words[self.index]
        except IndexError as exc:
            raise StopIteration() from exc

        self.index +=1
        return word

if __name__ == "__main__":
    s = WrongSentenceIterableIterator('"The time has come," the Walrus said,')
    print(s)

    iterator_1 = iter(s)
    iterator_2 = iter(s)

    print(next(iterator_1)) # -> The
    print(next(iterator_2)) # -> time

