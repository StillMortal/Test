"""
Given a cell with "it's a fib sequence" from slideshow,
    please write function "check_fib", which accepts a Sequence of integers,
    and returns if the given sequence is a Fibonacci sequence
We guarantee, that the given sequence contain >= 0 integers inside.
"""


def check_fibonacci(data: list) -> bool:
    """Whether the sequence is a Fibonacci sequence.
    Args:
        data: Sequence.
    Returns:
        True if successful, False otherwise.
    """
    if isinstance(data, str):
        data = (int(i) for i in data.split())
    else:
        data = (int(i) for i in data)
    previous = 0
    current = 1
    for pos, elem in enumerate(data):
        if pos == 0:
            if elem != previous:
                return False
        elif pos == 1:
            if elem != current:
                return False
        else:
            previous, current = current, previous + current
            if elem != current:
                return False

    return True