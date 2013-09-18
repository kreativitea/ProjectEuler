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
    ''' Yields abundant numbers indefinitely. '''
    c = count(1)
    while True:
        i = c.next()
        if i < sum(divisors(i, inclusive=False)):
            yield i


class Primes(set):
    ''' The set of all prime numbers.  
    Automatically updates when you make comparisons.
    
    >>> p = Primes()
    >>> 5 in p
    True
    >>> 6 in p
    False
    >>> 509 in p
    True
    >>> 510 in p
    False
    >>> set([5, 1019]) <= p
    True
    >>> set([5, 1020]) <= p
    False
    '''
    def __ge__(self, y):
        self._set_update(y)
        return super(Primes, self).__ge__(y)

    def __le__(self, y):
        self._set_update(y)
        return super(Primes, self).__le__(y)

    def __gt__(self, y):
        self._set_update(y)
        return super(Primes, self).__gt__(y)

    def __lt__(self, y):
        self._set_update(y)
        return super(Primes, self).__lt__(y)

    def isdisjoint(self, s):
        self._set_update(s)
        return super(Primes, self).isdisjoint(s)

    def issubset(self, s):
        self._set_update(s)
        return super(Primes, self).issubset(s)

    def issuperset(self, s):
        self._set_update(s)
        return super(Primes, self).issuperset(s)

    def intersection(self, s):
        self._set_update(s)
        return super(Primes, self).intersection(s)

    def difference(self, s):
        self._set_update(s)
        return super(Primes, self).difference(s)

    def symmetric_difference(self, s):
        self._set_update(s)
        return super(Primes, self).symmetric_difference(s)

    def update(self, s):
        raise NotImplementedError("Primes set does not implement Update")

    def clear(self):
        raise NotImplementedError("Primes set does not allow deletion")

    def __contains__(self, y):
        try:
            assert isinstance(y, int)
        except AssertionError:
            raise ValueError("Not an integer")

        while y > self._last:
            next = self._primes.next()
            self._last = next
            self.add(next)
        return super(Primes, self).__contains__(y)

    def __init__(self, *args):
        self._primes = genprime()
        self._last = 0
        return super(Primes, self).__init__(*args)

    def _set_update(self, s):
        maxval = max(s)
        self.__contains__(maxval)
