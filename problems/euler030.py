import itertools
import time, sys, os, inspect
import timeit

from collections import deque
from collections import defaultdict

import eutility as eul


def problem026(maxd):
    """ A unit fraction contains 1 in the numerator. 
    
    The decimal representation of the unit fractions with denominators 2 to 10 are given
    1/2 = 0.5
    1/3 = 0.(3)
    1/4 = 0.25
    1/5 = 0.2
    1/6 = 0.1(6)
    1/7 = 0.(142857)
    1/8 = 0.125
    1/9 = 0.(1)
    1/10 = 0.1

    Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

    Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part. """
    threes = range(3, maxd, 3)
    sevens = range(7, maxd, 7)
    chklist = set(threes + sevens)
    chkdict = {}
    for i in chklist:
        chkdict[i] = str(1.0 / i)


def problem028(n):
    '''  Starting with the number 1 and moving to the right in a clockwise direction a 
    5 by 5 spiral is formed as follows:

     21 22 23 24 25
     20  7  8  9 10
     19  6  1  2 11
     18  5  4  3 12
     17 16 15 14 13

    It can be verified that the sum of the numbers on the diagonals is 101.

    What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way? '''
    n = (n-1)/2
    return sum([sum(range((r*2+1)**2-(r*2)*3, ((r*2+1)**2)+1, r*2)) for r in range(1, n+1)])+1

def problem030(n):
    """ Surprisingly there are only three numbers that can be written as the sum of 
    fourth powers of their digits:

    1634 = 1**4 + 6**4 + 3**4 + 4**4
    8208 = 8**4 + 2**4 + 0**4 + 8**4
    9474 = 9**4 + 4**4 + 7**4 + 4**4
    As 1 = 1**4 is not a sum it is not included.

    The sum of these numbers is 1634 + 8208 + 9474 = 19316.

    Find the sum of all the numbers that can be written as the sum of fifth powers 
    of their digits."""
