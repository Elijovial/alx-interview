#!/usr/bin/python3


''' A module that returns the minimum Operations it takes to
    get to n characters.

    Available operations:
        copy
        paste
'''


def minOperations(n):
    '''
    returns the minimum operations to get n H's
    '''

    if n <= 1:
        return (0)
    operations = 0
    factor = 2
    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1
    return (operations)
