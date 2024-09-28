import doctest

def my_add(x: int, y: int) -> int:
    """
    Add to integers.

    Examples
    --------
    >>> my_add(1, 2)
    3
    >>> my_add(0, 0)
    0
    >>> my_add(-1, 0)
    -1
    """

    return x + y

def divide(a, b):
    """
    Divides two numbers.

    Example:
    >>> divide(6, 2)
    3.0
    >>> divide(5, 0)
    Traceback (most recent call last):
    ...
    ZeroDivisionError: division by zero
    """

    return a / b
