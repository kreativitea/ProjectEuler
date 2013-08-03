from eutility.eusequence import genfib as fibonacci


def euler025(length):
    '''
    
    The Fibonacci sequence is defined by the recurrence relation:

    Fn = Fn1 + Fn2, where F1 = 1 and F2 = 1.
    Hence the first 12 terms will be:

    F1 = 1
    F2 = 1
    F3 = 2
    ...
    F10 = 55
    F11 = 89
    F12 = 144

    The 12th term, F12, is the first term to contain three digits.

    What is the first term in the Fibonacci sequence to contain 1000 digits?

    >>> euler025(3)
    12
    >>> euler025(1000)
    4782 '''

    for index, value in enumerate(fibonacci()):
        if len(str(value)) >= length:
            return index

