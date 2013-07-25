def euler013(n, data):
    ''' Large Sum
   
    Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.

    >>> euler013(10) 
    5537376230L
    '''
    return int(str(sum(data))[:n])