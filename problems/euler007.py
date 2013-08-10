from eutility.eusequence import genprime
from itertools import islice


def euler007(n):
    ''' 10001st prime
    
    By listing the first six prime numbers: 2, 3, 5, 7, 11,
    and 13, we can see that the 6th prime is 13.

    What is the 10001st prime number?
    
    >>> euler007(6)
    13
    >>> euler007(10001)
    104743
    '''
    return islice(genprime(), n-1, n).next()
