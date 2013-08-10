def euler030(power):
    '''Digit fifth powers
    
    Surprisingly there are only three numbers that can be written as the sum of 
    fourth powers of their digits:

    1634 = 1**4 + 6**4 + 3**4 + 4**4
    8208 = 8**4 + 2**4 + 0**4 + 8**4
    9474 = 9**4 + 4**4 + 7**4 + 4**4
    As 1 = 1**4 is not a sum it is not included.

    The sum of these numbers is 1634 + 8208 + 9474 = 19316.

    Find the sum of all the numbers that can be written as the sum of fifth powers 
    of their digits.
    
    >>> euler030(4)
    19316
    >>> euler030(5)
    443839
    '''
    return sum(n for n in xrange(2, 4 * (9 ** power)) if sum_of_power(n, power))


def sum_of_power(n, power):
    ''' Returns True if the sum of the power of the number is equal to the number. 
    
    >>> sum_of_power(1634, 4)
    True
    >>> sum_of_power(1635, 4)
    False
    '''
    return n == sum(int(i) ** power for i in str(n))
