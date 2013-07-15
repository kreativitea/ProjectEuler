import itertools
import time, sys, os, inspect
import timeit

import eutility as eul


def problem048(n, len_n):
    """ The series, 1**1 + 2**2 + 3*3 + ... + 10**10 = 10405071317.
    Find the last ten digits of the series, 1**1 + 2**2 + 3**3 + ... + 1000**1000. 
    
    >>> problem048(1000,10)
    ... '9110846700' """
    return str(sum([i ** i for i in xrange(1, n+1)]))[-len_n:]

