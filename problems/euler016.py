def euler016(exponent):
    ''' Power digit sum
    
    2**15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
    What is the sum of the digits of the number 2**1000?

    >>> euler016(15)
    26
    >>> euler016(1000)
    1366
    '''
    return sum(int(i) for i in str(2 ** exponent))