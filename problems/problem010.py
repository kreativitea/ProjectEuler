from itertools import count
from eutility import fibonacci

def euler001(ns, maxn):
    ''' If we list all the natural numbers below 10 that are 
    multiples of 3 or 5, we get 3, 5, 6 and 9. 
    
    The sum of these multiples is 23.

    Find the sum of all the multiples of 3 or 5 below 1000.'''
    return sum([i for i in xrange(maxn) if any([i % n == 0 for n in ns])])

def euler002(maxn):
    c = count()
    sum = 0
    while True:
        fib = fibonacci(c.next())
        if fib > maxn:
            return sum
        if fib % 2 == 0 :
            sum += fib


def euler003(test):
    pass