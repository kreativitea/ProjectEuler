def euler006(n):
    ''' Sum square difference

    The sum of the squares of the first ten natural numbers is,
    1**2 + 2**2 + ... + 102 = 385

    The square of the sum of the first ten natural numbers is,
    (1 + 2 + ... + 10)2 = 552 = 3025

    Hence the difference between the sum of the squares of the first ten
    natural numbers and the square of the sum is 3025  385 = 2640.

    Find the difference between the sum of the squares of the first one
    hundred natural numbers and the square of the sum.

    >>> euler006(10)
    2640
    >>> euler006(100)
    25164150
    '''
    sum_square = sum(i * i for i in xrange(1, n+1))
    square_sum = sum(xrange(1, n+1)) ** 2
    return square_sum - sum_square 