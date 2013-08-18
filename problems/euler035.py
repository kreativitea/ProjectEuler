from eutility.eumath import primes
from eutility.eumath import rotate
from itertools import count

def euler035(limit):
    ''' Circular primes
    
    The number, 197, is called a circular prime because all rotations of 
    the digits: 197, 971, and 719, are themselves prime.

    There are thirteen such primes below 100: 
    
    2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

    How many circular primes are there below one million?

    >>> euler035(100)
    13
    >>> euler035(1000000)
    55
    '''
    c = count()
    P = set(primes(limit))

    for i in P:
        if all(r in P for r in rotate(i)):
            c.next()

    return c.next()
