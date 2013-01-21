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
    if n < 2:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)



def stormprimes(n):
    ''' Written by Storm on activestate.
    http://code.activestate.com/recipes/366178-a-fast-prime-number-list-generator/#c19 '''
    s=range(0,n+1)
    s[1]=0
    bottom=2
    top=n//bottom
    while (bottom*bottom<=n):
            while (bottom<=top):
                    if s[top]:
                            s[top*bottom]=0
                    top-=1
            bottom+=1
            top=n//bottom
    return [x for x in s if x]

def wangprimes(n): 
    ''' Written by Wensheng Wang on actvestate.
    http://code.activestate.com/recipes/366178-a-fast-prime-number-list-generator  '''
    if n==2: 
        return [2]
    elif n<2: return []
    s=range(3,n+1,2)
    mroot = n ** 0.5
    half=(n+1)/2-1
    i=0
    m=3
    while m <= mroot:
        if s[i]:
            j=(m*m-3)/2
            s[j]=0
            while j<half:
                s[j]=0
                j+=m
        i=i+1
        m=2*i+3
    return [2]+[x for x in s if x]

def eppprimes():
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

def hanksprimes(n):
    ''' written by Robert William Hanks
    http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188 '''
    sieve = [True] * (n/2)
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i/2]:
            sieve[i*i/2::i] = [False] * ((n-i*i-1)/(2*i)+1)
    return [2] + [2*i+1 for i in xrange(1,n/2) if sieve[i]]

a = 'stormprimes(10000)'
b = 'wangprimes(10000)'
c = 'hanksprimes(10000)'
timeit(a, setup=timers, number=100)
timeit(b, setup=timers, number=100)
timeit(c, setup=timers, number=100)
