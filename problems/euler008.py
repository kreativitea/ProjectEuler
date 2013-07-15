from eutility.fileops import readfile
from operator import mul
from collections import deque

def euler008(n, filename):
    ''' Largest product in a series

    Find the greatest product of five consecutive digits
    in the 1000-digit number.

    >>> euler008(5, "euler008.txt")
    40824
    '''
    f = readfile(filename)
    with f:
        data = f.next()
        return max(reduce(mul, (int(data[i+j]) 
                                for i in xrange(0,n))) 
                                for j in xrange(len(data)-n))

def euler008a(n, filename):
    f = readfile(filename)
    with f:
        data = iter(f.next())
        return max(reduce(mul, i) for i in spitter(data, n))

def spitter(iterator, n, f=int):
    d = deque((f(iterator.next()) for i in xrange(n)), n)
    while True:
        yield d
        d.append(f(iterator.next()))
