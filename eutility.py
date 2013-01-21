def memodict(f):
    """ Memoization decorator for a function taking a single argument """
    class memodict(dict):
        def __missing__(self, key):
            ret = self[key] = f(key)
            return ret 
    return memodict().__getitem__

def memoize(f):
    """ Memoization decorator for a function taking one or more arguments. """
    class memodict(dict):
        def __getitem__(self, *key):
            return dict.__getitem__(self, key)

        def __missing__(self, key):
            ret = self[key] = f(*key)
            return ret

    return memodict().__getitem__

@memodict
def fibonacci(n):
    ''' Returns n values of the fibonacci sequence.'''
    if n < 2:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def genprimes():
    ''' Written by David Eppstein, UCI Irvine. 
    Continuously yields primes.
    http://code.activestate.com/recipes/117119-sieve-of-eratosthenes/ '''
    yield 2
    D = {}
    c = 3
    while True:
        s = D.pop(c, 0)
        if s:
            add(D,c + s,s)
        else:
            yield c
            D[c*c] = 2*c
        c += 2

def primes(n):
    ''' written by Robert William Hanks
    http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188 '''
    sieve = [True] * (n/2)
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i/2]:
            sieve[i*i/2::i] = [False] * ((n-i*i-1)/(2*i)+1)
    return [2] + [2*i+1 for i in xrange(1,n/2) if sieve[i]]