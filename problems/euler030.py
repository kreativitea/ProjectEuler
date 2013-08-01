import itertools
import time, sys, os, inspect
import timeit

from collections import deque
from collections import defaultdict

import eutility as eul



def problem022(filename):
    """ Using problem022.txt, a 46K text file containing over five-thousand first names, 
    begin by sorting it into alphabetical order. Then working out the alphabetical value 
    for each name, multiply this value by its alphabetical position in the list to obtain 
    a name score.

    For example, when the list is sorted into alphabetical order, COLIN, which is worth 
    3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a 
    score of 938  53 = 49714.

    What is the total of all the name scores in the file? 
    >>> problem022("problem022.txt")
    ... 871198282 """
    f = open(filename)
    text = [i.replace('"', '') for i in f.read().split(',')]
    f.close()
    text = sorted(text)
    total = 0
    for nameindex in xrange(len(text)):
        total += sum([return_letter(i) for i in text[nameindex]]) * (nameindex + 1)
    return total

def problem023():
    """ A perfect number is a number for which the sum of its proper divisors is exactly 
    equal to the number. For example, the sum of the proper divisors of 28 would be 
    
    1 + 2 + 4 + 7 + 14 = 28, 
    
    which means that 28 is a perfect number.

    A number n is called deficient if the sum of its proper divisors is less than n and it 
    is called abundant if this sum exceeds n.

    As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that 
    can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can
    be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. 
    However, this upper limit cannot be reduced any further by analysis even though it is known 
    that the greatest number that cannot be expressed as the sum of two abundant numbers is less 
    than this limit.

    Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers. """
    lim = 28123
    abundant = {}
    for i in xrange(lim):
        a = eul.return_divisors_sum(i)
        if i < a:
            abundant[i] = a
    
    results = []

    def test_abundant(n):
        for i in abundant:
            test_n = i - n
            if test_n in abundant:
                return True
        return False

    for i in xrange(lim):
        test_abundant(i)

                






def problem024(n, digits):
    """ A permutation is an ordered arrangement of objects. For example, 3124 is one 
    possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are 
    listed numerically or alphabetically, we call it lexicographic order. The lexicographic 
    permutations of 0, 1 and 2 are:

    012   021   102   120   201   210

    What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9? 
    
    >>> problem024(1000000,9)
    ... '2783915460' """
    permutations = itertools.permutations(range(digits + 1))
    s = 0
    for i in xrange(n):
        s = permutations.next()
    return "".join([str(i) for i in s])

def problem025(len_n):
    """The Fibonacci sequence is defined by the recurrence relation:

    Fn = Fn1 + Fn2, where F1 = 1 and F2 = 1.
    Hence the first 12 terms will be:

    F1 = 1
    F2 = 1
    F3 = 2
    
    F10 = 55
    F11 = 89
    F12 = 144
    The 12th term, F12, is the first term to contain three digits.

    What is the first term in the Fibonacci sequence to contain 1000 digits?
    >>> problem025(1000)
    ... 4782 """
    n = [1, 2]
    while len(str(n[-1])) < len_n:
        n.append(n[-1] + n[-2])
    return len(n)+1


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
    """  Starting with the number 1 and moving to the right in a clockwise direction a 
    5 by 5 spiral is formed as follows:

     21 22 23 24 25
     20  7  8  9 10
     19  6  1  2 11
     18  5  4  3 12
     17 16 15 14 13

    It can be verified that the sum of the numbers on the diagonals is 101.

    What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way? """
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
