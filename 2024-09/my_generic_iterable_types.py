from collections.abc import Iterable, Iterator
from typing import Tuple

FromTo = Tuple[str, str]

def zip_replace(text: str, changes: Iterable[FromTo]) -> str:
    for from_, to in changes:
        text = text.replace(from_, to)
    return text

def fibonacci() -> Iterator[int]:
    a, b = 0, 1
    while True:
        yield a + b
        a, b = b, a+b

"""
The type `Iterator` is used for generators coded as functions with `yield` as well
as iterators written `by hand` as classes with `__next__`. There is also a
`collections.abc.Generator` Type (adn the corresponding deprecated typing.Generator)
that we can use to annotate generator objects, but it is needlessly verbose for generators used as iterators.

When checked with Mypy, reveals that the Iterator type is really a simplified special case of `Generator` type
"""

from collections.abc import Iterator
from keyword import kwlist
from typing import TYPE_CHECKING, reveal_type

short_kw = (k for k in kwlist if len(k) < 5)
if TYPE_CHECKING:
    reveal_type(short_kw)

long_kw: Iterator[str] = (k for k in kwlist if len(k) >= 5)
if TYPE_CHECKING:
    reveal_type(long_kw)

"""
abc.Iterator[str] is consistent-with abc.Generator[str, None, None], therefore, Mypy issues no errors for type checking.
"""

"""
Iterator[T] is a shortcut for Generator[T, None, None]. Both annotations mean "a generator that yields items of type `T`".
but that does not consume or return values.

Generators able to consume and return values are coroutines.

"""