from collections import namedtuple
from eutility.eumath import even


def euler014(limit):
    ''' Longest Collatz sequence

    The following iterative sequence is defined for the set of positive integers:

    n => n/2 (n is even)
    n => 3n + 1 (n is odd)

    Using the rule above and starting with 13, we generate the following sequence:

    13  40  20  10  5  16  8  4  2  1

    It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. 
    Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

    Which starting number, under one million, produces the longest chain?

    NOTE: Once the chain starts the terms are allowed to go above one million. 
    
    # Quite inefficient, takes some time.  May need to be recoded.

    >>> problem014(1000000)
    837799
    '''

    # result: unit, length
    Collatz = namedtuple("Col", "res, len")
    colcache = {1: Collatz(1, 1)}

    def collatz(n):
        if even(n):
            return n/2
        else:
            return 3 * n + 1

    def add_col(n, colcache):
        dist = 0
        nd = n
        while True:
            if nd not in colcache:
                nd = collatz(nd)
                dist += 1
            else:
                break
        total_dist = colcache[nd].len + dist
        colcache[n] = Collatz(collatz(n), total_dist)
        return total_dist
    
    max_col = 0
    candidate = 0
    for i in xrange(1, limit):
        dist = add_col(i, colcache)
        if dist > max_col:
            max_col, candidate = dist, i
    return candidate