from eutility import memodict
import math
import operator
from operator import mul

@memodict
def fibonacci(n):
    ''' Returns n values of the fibonacci sequence. '''
    if n < 2:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# written by Robert William Hanks
# http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
def primes(n):
    ''' Generates all the prime numbers up to n.
    
    >>> primes(10)
    [2, 3, 5, 7]
    >>> primes(75)
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73]
    '''
    sieve = [True] * (n/2)
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i/2]:
            sieve[i*i/2::i] = [False] * ((n-i*i-1)/(2*i)+1)
    return [2] + [2*i+1 for i in xrange(1,n/2) if sieve[i]]


def even(n):
    ''' Returns True if n is even. 

    >>> even(2)
    True
    >>> even(5)
    False
    '''
    return not bool(n % 2)


def odd(n):
    ''' Returns True if n is odd. 
    
    >>> odd(2)
    False
    >>> odd(5)
    True
    '''
    return bool(n % 2)


def insert_list(o, i, p):
    ''' Inserts a list p into an index location of o

    >>> o = [1, 2, 3, 4, 5]
    >>> p = ['a', 'b', 'c']
    >>> insert_list(o, 0, p)
    ['a', 'b', 'c', 1, 2, 3, 4, 5]
    >>> insert_list(o, 1, p)
    [1, 'a', 'b', 'c', 2, 3, 4, 5]
    >>> insert_list(o, -1, p)
    [1, 2, 3, 4, 'a', 'b', 'c', 5]
    '''
    right = o[i:]
    left = o[:i]
    return left + p + right


def palindrome(iterable):
    ''' Checks to see if something is a palindrome. 
    
    >>> pal = 123321
    >>> palindrome(pal)
    True
    >>> notpal = 12343214
    >>> paldindrome(notpal)
    False
    '''
    return str(iterable) == str(iterable)[::-1]


def prime_factors(n):
    ''' Lists prime factors, from greatest to smallest. 

    >>> prime_factors(12)
    [3, 2, 2]
    >>> prime_factors(256)
    [2, 2, 2, 2, 2, 2, 2, 2]
    '''
    i = 2
    while i <= math.sqrt(n):
        if n % i == 0:
            l = prime_factors(n/i)
            l.append(i)
            return l
        i += 1
    return [n]


def divisors(n, inclusive=True):
    ''' Generates all divisors, unordered. 

    >>> list(divisors(12))
    [1, 2, 4, 3, 6, 12]
    >>> list(divisors(256))
    [1, 2, 4, 8, 16, 32, 64, 128, 256]
    '''
    if n == 1:
        yield 1

    else:
        factors = prime_factors(n)
        ps = sorted(set(factors))
        omega = len(ps)

        def divisor_generator(n=0):
            if n == omega:
                yield 1
            else:
                pows = [1]
                for j in xrange(factors.count(ps[n])):
                    pows += [pows[-1] * ps[n]]
                for q in divisor_generator(n + 1):
                    for p in pows:
                        yield p * q
    
        for p in divisor_generator():
            if inclusive:
                yield p
            if not inclusive:
                if p != n:
                    yield p


def is_prime(n):
    ''' Returns true if n is prime. '''
    primes = return_primes_list(n)
    if n in primes:
        return True
    else:
        return False


def collatz(n):
    length = 1
    while n != 1:
        if even(n):
            n = n/2
        else:
            n = 3 * n + 1
        length += 1
    return length


def collatz_list(n):
    length = 1
    p = []
    while n != 1:
        if even(n):
            n = n/2
        else:
            n = 3 * n + 1
        length += 1
        p.append(n)
    return length, p


def letter(a):
    ''' Returns the alphabetical position of a; e.g. A = 1, B = 2.
    Accepts both upper and lower case letters. 
    Raises a type error if not a letter.

    >>> return_letter('a')
    1
    >>> return_letter('z')
    26
    >>> return_letter('A')
    1
    >>> return_letter('Z')
    26
    >>> try:
    ...     return_letter('!')
    ... except TypeError:
    ...     print "TypeError"
    TypeError
    '''
    n = ord(a.upper())-ord('A')+1
    if 0 < n < 27:
        return n
    else:
        raise TypeError('Does not accept non-letter arguments')


def return_triangle_list(n):
    sums = []
    sum = 0
    for i in xrange(1, n+1):
        sum += i
        sums.append(sum)
    return sums


def factorial(n):
    ''' Returns the factorial of n. 
    >>> factorial(5)
    120
    >>> factorial(7)
    5040
    '''
    return math.factorial(n)


def stringbin(n):
    ''' Returns a string representing the binary of a number. 
    >>> stringbin(2)
    '10'
    >>> stringbin(256)
    '100000000'
    >>> stringbin(255)
    '11111111'
    >>> stringbin(10)
    '1010'
    '''
    return bin(n)[2:]
