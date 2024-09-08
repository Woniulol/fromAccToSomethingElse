"""
We want to generate an arithmetic progression of numbers of any type, not only integers.

>>> ap = ArithmeticProgression(0, 1, 3)
>>> list(ap)
[0, 1, 2]
>>> ap = ArithmeticProgression(1, .5, 3)
>>> list(ap)
[1.0, 1.5, 2.0, 2.5]
>>> ap = ArithmeticProgression(0, 1/3, 1)
>>> list(ap)
[0.0, 0.3333333333333333, 0.6666666666666666]
>>> from fractions import Fraction
>>> ap = ArithmeticProgression(0, Fraction(1, 3), 1)
>>> list(ap)
[Fraction(0, 1), Fraction(1, 3), Fraction(2, 3)]
>>> from decimal import Decimal
>>> ap = ArithmeticProgression(0, Decimal('.1'), .3)
>>> list(ap)
[Decimal('0'), Decimal('0.1'), Decimal('0.2')]
"""

class ArithmeticProgression:

    def __init__(self, begin, step, end=None) -> None:
        self.begin = begin
        self.step = step
        self.end = end

    def __iter__(self):
        result_type = type(self.begin + self.step)
        result = result_type(self.begin)
        forever = self.end is None
        index = 0

        while forever or result < self.end:
            yield result

            index += 1
            result = self.begin + self.step * index

"""
Since the whole purpose of ArithmeticProgression is to generate a generator, we can use a generator function.
"""

def aritprog_gen(begin, step, end=None):
    result = type(begin + step)(begin)
    forever = end is None
    index = 0
    while forever or result < end:
        yield result
        index += 1
        result = begin + step * index

import itertools

gen = itertools.count(1, .5)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

gen = itertools.takewhile(lambda n: n < 3, itertools.count(1, .5))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

def aritprog_gen(begin, step, end=None):
    first = type(begin + step)(begin)
    ap_gen = itertools.count(first, step)
    if end is None:
        return ap_gen
    return itertools.takewhile(lambda n: n < end, ap_gen)