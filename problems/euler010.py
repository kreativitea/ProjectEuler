from eutility.eusequence import genprime
from itertools import takewhile

def euler010(limit):
    ''' The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
    Find the sum of all the primes below two million. 
    
    >>> euler010(10)
    17
    >>> euler010(2000000)
    142913828922L
    '''
    primes = genprime()
    return sum(takewhile(lambda x: x < limit, primes))
