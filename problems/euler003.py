from eutility.eumath import prime_factors


def euler003(n):
    ''' Largest prime factor
    
    What is the largest prime factor of the number 600851475143?

    >>> print euler003(600851475143)
    6857
    '''
    return max(int(i) for i in prime_factors(n))
