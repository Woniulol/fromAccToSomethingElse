"""
An `iterable` is an object that provides an `iterator`.
Objects implementing an `__iter__` method returning aiterator are iterable.

Python obtains iterators from iterables.

Sequences are iterable:

Whenever Python needs to iterate over an object `x`, it automatically calls `iter(x)`

`iter()` will then:
1. Check whether the object implements `__iter__` and calls that to obtain an iterator.
2. If `__iter__` is not implemented, but `__getitem__` is, then `iter()` crates an iterator that tries to fetch items by index, starting from 0 (zero).
3. If that fails, Python raises `TypeError`, saying class of `x` is not iterable.

That is to say, an object is considered iterable not only when it implements the `__iter__`, but also when it implements `__getitem__`.
Thus, to check if an object is iterable, the most accurate way is to use `iter(x)` as it check both `__iter__` and `__getitem__`.

To check if an object is iterator, call `isinstance(x, abc.Iterator)`

But, without `__iter__`, instance will not be considered as an instance of `abc.Iterable`.

`iter()` can also be used (and more often be used) to create an iterator from a function or any callable object with two arguments:
1. A callable to be invoked repeatedly (with no arguments) to produce values.
2. A sentinel (a marker value which, when returned by the callable, causes the iterator to raise `StopIteration` instead of yielding the sentinel.)

Often use `partial` to make the callable require no arguments

Python's standard interface for an iterator has two methods:
1. `__next__`:
    Returns the next item in the series, raising `StopIteration` if there are no more.
2. `__iter__`:
    Returns `self`; this allows iterators to be used where an iterable is expected, for example, in a for loop.

That interface is formalized in the `collections.abc.Iterator`
"""

from random import randint
import re
import reprlib

RE_WORD = re.compile(r"\w+")


class Sentence:

    def __init__(self, text) -> None:
        self.text = text
        self.words = RE_WORD.findall(text)

    def __getitem__(self, index):
        return self.words[index]

    def __len__(self):
        return len(self.words)

    def __repr__(self):
        return f"Sentence({reprlib.repr(self.text)})"


def d6():
    return randint(1, 7)


if __name__ == "__main__":
    s = Sentence('"The time has come," the Walrus said,')
    print(s)

    for word in s.words:
        print(word)

    print(list(s))


    # d6_iter is a `callable_iterator`
    d6_iter = iter(d6, 1)
    for roll in d6_iter:
        print(roll)

    # If we dont have the `for`` statement to get the iterator for us, we
    # can implement `for` manually.
    string = "ABC"
    it = iter(string)
    while True:
        try:
            print(next(it))
        except StopIteration:
            del it
            break
