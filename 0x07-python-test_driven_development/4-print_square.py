#!/usr/bin/python3
"""definition of a function that print squares"""


def print_square(size):
    """printing a square using # characters"""

    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    elif size < 0:
        raise ValueError('size must be >= 0')
    print('\n'.join(['#' * size] * size))
