def euler001(ns, limit):
    ''' Multiples of 3 and 5

    If we list all the natural numbers below 10 that are 
    multiples of 3 or 5, we get 3, 5, 6 and 9. 
    
    The sum of these multiples is 23.

    Find the sum of all the multiples of 3 or 5 below 1000.
    
    >>> euler001((3, 5), 10)
    23
    >>> euler001((3, 5), 1000)
    233168
    '''
    return sum(i for i in xrange(limit) if any(i % n == 0 for n in ns))
