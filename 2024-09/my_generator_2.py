"""
Lazy Generator

The `Iterator` interface is designed to be lazy. `next(my_iterator)` yields on item at a time.
The opposite of lazy is eager.

We can make the words to be a generator rather than load all the words in the memory when the instance is institutionalized.

We can make a even further step to make the generator function to be a generator comprehension (expression)

Iterator and Generator:

Iterator is the general term for any object that implements a `__next__` method. Iterators are designed to product data that is consumed by the client code.
That is to say, th ecode that drived the iterator via a `for` loop or other iterative features, or by explicit calling next(it) on the iterator, although this explicit
usage is a much less common. In practice, most iterators we use in Python are generators.

Generators is an iterator built by Python compiler. To create a generator, we don't implement `__next__`. Instead, we use the yield keyword to make a generator function,
which is a factory of `generator objects`. A `generator expression` is another way to build a generator object. Generator objects provide `__next__`, so they are iterators.

Generator iterator is generator objects built by generator functions, while the entry of generator expression says it returns an `iterator`.


"""

import re
import reprlib

RE_WORD = re.compile(r"\w+")


class Sentence:

    def __init__(self, text):
        self.text = text

    def __repr__(self):
        return f"Sentence({reprlib.repr(self.text)})"

    # def __iter__(self):
    #     for match in RE_WORD.finditer(self.text):
    #         yield match.group()

    def __iter__(self):
        return (match.group() for match in RE_WORD.finditer(self.text))
