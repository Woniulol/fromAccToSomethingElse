"""
Any Python function that has they `yield` keyword in its body is a generator function.

A generator function is the function which, when called, returns a generator object.
That is to say, a generator function is a generator factory.

Generator objects implement the `Iterator` interface, so they are also iterable.

When the generator function return, the generator raise `StopIteration`

A generator function builds a generator object that wraps the body of the function.

Functions return values.
Calling a generator function returns a generator.
A generator yields values, but does not "return" values in the usual way.
The `return` statement in the body of a generator function causes `stopIteration` to be raised by the generator object.

If you `return x` in the generator, the caller can retrieve the value of `x` from the StopIteration exception, btu usually that is done automatically using the yield from syntax.

"""

def gen_AB():
    print("Start")
    yield "A"
    print("Continue")
    yield "B"
    print("end.")


count = 0
for c in gen_AB():
    print(count)
    print("-->", c)
    count += 1

"""
Start -> comes from print("Start") in the generator body, which is before the first implict `next()` call (before the for loop).
0
--> A
Continue
1
--> B
end.
"""

"""
To iterate, the `for` machinery does the equivalent of `g == iter(gen_AB())` to get
a new generator object, and then next(g) at each iteration.
"""