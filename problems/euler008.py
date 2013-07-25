from eutility.fileops import readfile
from operator import mul
from collections import deque


def euler008(n, data):
    ''' Largest product in a series

    Find the greatest product of five consecutive digits
    in the 1000-digit number.
    
    >>> from eutility.fileops import readfile
    >>> with readfile('euler008.txt') as f:
    >>> n, data = int(f.next()), f.next()
    >>> euler008(5, data)
    40824
    '''

    return max(reduce(mul, (int(data[i+j]) 
                            for i in xrange(0,n))) 
                            for j in xrange(len(data)-n))
