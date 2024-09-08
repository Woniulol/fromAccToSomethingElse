"""
The implementation of iterator looks pretty complex and dummy.

A Pythonic implementation of the same functionality uses a generator, avoiding all the works
to implement a separated `SentenceIterator`

"""

import re
import reprlib

RE_WORD = re.compile(r"\w+")


class Sentence:

    def __init__(self, text) -> None:
        self.text = text
        self.words = RE_WORD.findall(text)

    def __repr__(self):
        return f"Sentence({reprlib.repr(self.text)})"

    def __iter__(self):
        """
        Now the iterator returned by `__iter__` is in fact a generator object, built automatically when the `__iter__` method is called,
        because `__iter__` here is a generator function.
        """
        for word in self.words:
            yield word

if __name__ == "__main__":
    s = Sentence('"The time has come," the Walrus said,')
    print(s)

    iterator_1 = iter(s)
    iterator_2 = iter(s)

    print(next(iterator_1)) # -> The
    print(next(iterator_2)) # -> The

    print(next(iterator_1)) # -> The
    print(next(iterator_2)) # -> The
