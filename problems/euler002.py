from itertools import ifilter, takewhile
from eutility.eusequence import genfib as fibonacci
from eutility.eumath import even


def euler002(maxterm):
    ''' Even Fibonacci numbers
   
    Each new term in the Fibonacci sequence is generated by adding the previous two terms. 
    
    By starting with 1 and 2, the first 10 terms will be:
    1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

    By considering the terms in the Fibonacci sequence whose values do not exceed four million, 
    find the sum of the even-valued terms.
    
    >>> euler002(100)
    44

    >>> euler002(4000000)
    4613732
    '''
    fib = fibonacci()
    return sum(ifilter(even, takewhile(lambda x: x < maxterm, fib)))