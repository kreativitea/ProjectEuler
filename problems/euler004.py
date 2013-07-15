from itertools import product, repeat, izip, takewhile
from eutility.eumath import palindrome


def euler004(digits):
    ''' Largest palindrome product
    
    A palindromic number reads the same both ways. The largest palindrome
    made from the product of two 2-digit numbers is 9009 = 91 * 99.

    Find the largest palindrome made from the product of two 3-digit numbers.
    
    >>> euler004(2)
    9009

    >>> euler004(3)
    906609
    '''

    for i in xrange(10 ** digits-1, 0, -1):
        r = xrange(10 ** digits-1, i-1, -1)
        try:
            return max(j * k for j, k in
                       takewhile(lambda x: x[0] >= x[1], izip(r, reversed(r)))
                       if palindrome(str(j * k)) and not j % 11)
        except ValueError:
            pass

def test_euler004():
    results = [None, 9, 9009, 906609, 99000099, 9966006699L, 999000000999L, 99956644665999L]
    for i in range(8):
        assert euler004(i) == results[i]
    print 'passed all tests!'

def euler004a(digits):
    ''' Largest palindrome product
    
    Brute force method.
    
    >>> euler004a(2)
    9009

    >>> euler004(3)
    906609
    '''
    return max(x*y for x in xrange(10 ** (digits-1), 10 ** digits) 
               for y in xrange(10 ** (digits-1), 10 ** digits) 
               if palindrome(str(x*y)))
