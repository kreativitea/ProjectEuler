import itertools
import time, sys, os, inspect
import timeit
from collections import Counter
from collections import defaultdict
from collections import namedtuple

import eutility as eul

    
def problem015(n):
    """ Starting in the top left corner of a 2 x 2 grid, there are 6 routes (without backtracking) to the bottom right corner.
    How many routes are there through a 20 x 20 grid? """
    pass


def problem016(expo):
    """2**15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
    What is the sum of the digits of the number 2**1000?
    
    >>> problem016(1000)
    ... 1366 """
    return sum(int(i) for i in str(2 ** expo))

def problem017(start, num): #unsolved
    """ If the numbers 1 to 5 are written out in words: one, two, three, four, five, 
    then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

    If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, 
    how many letters would be used? 
    >>> problem017(1,1000)
    ... 21124 """
    number_dict = {0: '', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
                   6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
                   11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen',
                   16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen', 20: 'twenty',
                   30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty', 
                   90: 'ninety', 100: 'onehundred', 200: 'twohundred', 300: 'threehundred', 400: 'fourhundred', 
                   500: 'fivehundred', 600: 'sixhundred', 700: 'sevenhundred', 800: 'eighthundred', 
                   900: 'ninehundred', 1000: 'onethousand'}

    def return_len(n):
        """ Only works up to 1000.  """
        try:
            value = number_dict[n]
            length = len(value)
        except KeyError:
            ones = n % 10
            tens = n % 100 - ones
            hundreds = n % 1000 - tens - ones
            if tens == 10:
                tens = ones + tens
                ones = 0
            if n > 100:
                conjunction = "and"
            else:
                conjunction = ""
            value = "".join([number_dict[hundreds], conjunction, number_dict[tens], number_dict[ones]])
            length = len(value)
        finally:
            return length

    return sum([return_len(i) for i in xrange(start, num+1)])

def problem018():
    testtriangle = """ 3
                       7 4
                       2 4 6
                       8 5 9 3 """

    triangle = """ 75
                   95 64
                   17 47 82
                   18 35 87 10
                   20 04 82 47 65
                   19 01 23 75 03 34
                   88 02 77 73 07 63 67
                   99 65 04 28 06 16 70 92
                   41 41 26 56 83 40 80 70 33
                   41 48 72 33 47 32 37 16 94 29
                   53 71 44 65 25 43 91 52 97 51 14
                   70 11 33 28 77 73 17 78 39 68 17 57
                   91 71 52 38 17 14 91 43 58 50 27 29 48
                   63 66 04 68 89 53 67 30 73 16 69 87 40 31
                   04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""

    pyramid = [[int(n) for n in i.split()] for i in triangle.split("\n")]
    testpyramid = [[int(n) for n in i.split()] for i in testtriangle.split("\n")]



def problem019(): #unsolved
    pass


def problem020(n):
    result = str(eul.factorial(n))