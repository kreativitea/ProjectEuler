from itertools import count
from eumath import divisors


def genfib():
    ''' Yields fibonacci numbers indefinitely. '''
    x, y = 0, 1
    while True:
        yield x
        x, y = y, x+y


# Written by Will Ness  
# http://code.activestate.com/recipes/117119-sieve-of-eratosthenes/
def genprime():
    ''' Yields prime numbers indefinitely. '''
    yield 2; yield 3; yield 5; yield 7;
    D = {}
    c = 9
    ps = (p for p in genprime())
    p = ps.next() and ps.next()
    q = p * p
    while True:
        if c not in D:
            if c < q: yield c
            else:
                _add(D, c + 2*p, 2*p)
                p = ps.next()
                q = p * p
        else:
            s = D.pop(c)
            _add(D, c + s, s)
        c += 2

def _add(D, x, s):
  while x in D: x += s
  D[x] = s


def gentriangle():
    ''' Yields triangle numbers indefinitely. '''
    triangle = 0
    i = 1
    while True:
        triangle = triangle + i
        i += 1
        yield triangle


def abundant():
    c = count(1)
    while True:
        i = c.next()
        if i < sum(divisors(i, inclusive=False)):
            yield i
