import itertools
import time, sys, os, inspect
import timeit

import eutility as eul


def problem036(nmax):
    """ The decimal number, 585 = 1001001001_2 (binary), is palindromic in both bases.

    Find the sum of all numbers, less than one million, which are palindromic in base 10 
    and base 2.

    (Please note that the palindromic number, in either base, may not include leading zeros.)
    
    >>> problem036(1000000)
    ... 872187
    """
    sum = 0
    for i in xrange(1, nmax, 2):
        if all([eul.is_palindrome(i), eul.is_palindrome(eul.stringbin(i))]):
            sum += i
    return sum