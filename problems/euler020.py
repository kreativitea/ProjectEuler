from eutility.eumath import factorial


def euler020(n):
    ''' Factorial digit sum

    n! means n * (n ? 1) * ... * 3 * 2 * 1

    For example, 10! = 10 * 9 * ... * 3 * 2 * 1 = 3628800,
    and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

    Find the sum of the digits in the number 100!

    >>> euler020(10)
    27
    >>> euler020(100)
    648
    '''
    return sum(int(i) for i in str(factorial(n)))
