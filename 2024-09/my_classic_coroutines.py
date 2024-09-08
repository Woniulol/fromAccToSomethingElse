"""
Classic Coroutine is different from Native Coroutine

Classic Coroutine is generators that could use `.send()` and other features that made it possible to use generators as coroutines.

Classic Coroutine is not supported by `asyncio` anymore after Python 3.5

A `coroutine` is really a generator function, created with `yield` keyword in its body.
A `coroutine object` is physically a generator object.
"""

# The `readings` variable can be bound to an iterator
# or generator object that yields `float` items:
from asyncio import Event
from typing import Generator, Iterator


readings: Iterator[float]

# The `sim_taxi` variable can be bound to a coroutine
# representing a taxi cab in a discrete event simulation.
# It yields events, receives `float` timestamps, and returns
# the number of trips made during the simulation:
sim_taxi: Generator[Event, float, int]


# The formal type parameters of Generator:
# Generator[YieldType, SendType, ReturnType]
# It is the same as typing.Coroutine (now deprecated and replaced by collections.abc.Coroutine)
# Coroutine[YieldType, SendType, ReturnType]

# But Coroutine[YieldType, SendType, ReturnType] is ONLY meant for the native coroutine, not the classic one.

# Coroutine to compute a running average
def averager() -> Generator[float, float, None]:
    print("Inside")
    total = 0.0
    count = 0
    average = 0.0
    while True:
        term = yield average
        total += term
        count += 1
        average = total / count

"""
In  coroutine, `total` and `count` can be local varibales. No instance attibutes or closures are needed to keep the context while the coroutine is suspended waiting for the next `.send()`
That's why corountines are attractive replacements for callbacks in asynchronous programming, they keep local state between activatetion.
"""

coro_avg = averager()
print(next(coro_avg)) # equals to coro_avg.send(None)
print(coro_avg.send(10))
print(coro_avg.send(30))
print(coro_avg.send(5))

from collections.abc import Generator
from typing import Union, NamedTuple

class Result(NamedTuple):
    count: int  # type: ignore
    average: float

class Sentinel:
    def __repr__(self):
        return f'<Sentinel>'

STOP = Sentinel()
SendType = Union[float, Sentinel]

def averager2(verbose: bool = False) -> Generator[None, SendType, Result]:
    total = 0.0
    count = 0
    average = 0.0
    while True:
        term = yield
        if verbose:
            print('received:', term)
        if isinstance(term, Sentinel):
            break
        total += term
        count += 1
        average = total / count
    return Result(count, average)

coro_avg = averager2(verbose=True)
next(coro_avg)
coro_avg.send(10)
coro_avg.send(30)
coro_avg.send(6.5)
try:
    coro_avg.send(STOP)
except StopIteration as exc:
    result = exc.value

print(result)
coro_avg.close()

