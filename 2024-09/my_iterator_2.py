import re
import reprlib

RE_WORD = re.compile(r"\w+")

class Sentence:

    def __init__(self, text) -> None:
        self.text = text
        self.words = RE_WORD.findall(text)

    def __repr__(self):
        return f'Sentence({reprlib.repr(self.text)})'

    def __iter__(self):
        return SentenceIterator(self.words)


class SentenceIterator:

    def __init__(self, words) -> None:
        self.words = words
        self.index = 0

    def __next__(self):
        try:
            word = self.words[self.index]
        except IndexError as exc:
            raise StopIteration() from exc

        self.index +=1
        return word

    def __iter__(self):
        """
        This is not actually needed for the example to work.

        But this is the right thing to do as iterators are supposed to implement both `__next__` and `__iter__`
        to pass the `issubclass(SentenceIterator, abc.Iterator)` test.

        If we had subclassed SentenceIterator from abc.Iterator, we'd inherit the concrete abc.Iterator.__iter__ method, which
        returns itself anyway.
        """
        return self


