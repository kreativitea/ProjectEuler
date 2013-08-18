def euler048(n, length):
    ''' The series, 1**1 + 2**2 + 3*3 + ... + 10**10 = 10405071317.
    Find the last ten digits of the series, 1**1 + 2**2 + 3**3 + ... + 1000**1000. 
    
    >>> euler048(1000,10)
    '9110846700'
    '''
    return str(sum(i ** i for i in xrange(1, n+1)))[-length:]

