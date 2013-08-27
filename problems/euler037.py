from eutility.eusequence import genprime as prime
from collections import deque
from itertools import repeat, chain

def euler037(n):
    ''' Truncatable primes
    
    The number 3797 has an interesting property. Being prime itself,
    it is possible to continuously remove digits from left to right,
    and remain prime at each stage: 3797, 797, 97, and 7. Similarly we
    can work from right to left: 3797, 379, 37, and 3.

    Find the sum of the only eleven primes that are both truncatable
    from left to right and right to left.

    NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
    
    >>> euler037(11)
    748317
    '''
    results = set(['2', '3', '5', '7'])
    p = prime()
    primes = set()
    while len(results) < (n + 4):
        next = str(p.next())
        primes.add(next)
        if all(i in primes for i in truncate(next) if i != next):
            results.add(next)
    return sum(int(i) for i in results) - sum([2, 3, 5, 7])

def truncate(n):
    ''' Performs the truncate operation for euler037.
    
    >>> list(truncate(3797))
    ['3', '37', '379', '3797', '797', '97', '7']
    '''
    n = str(n)
    c = chain(iter(n), repeat('', len(n)-1))
    d = deque('', maxlen=len(n))
    while True:
        d.append(c.next())
        yield ''.join(d)