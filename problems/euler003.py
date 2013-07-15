from eutility.eumath import primes


def euler003(n):
    ''' Largest prime factor
    
    What is the largest prime factor of the number 600851475143?

    >>> print euler003(600851475143)
    6857
    '''
    for i in primes(2000): # checks up to 2000 primes
        if n % i == 0:
            n = n/i
    return n
