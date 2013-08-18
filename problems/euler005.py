from eutility.eumath import divisors


def euler005(n):
    ''' Smallest multiple

    2520 is the smallest number that can be divided by each of the numbers from 1 to
    10 without any remainder.

    What is the smallest positive number that is evenly divisible by all of the numbers
    from 1 to 20?

    >>> euler005(10)
    2520
    >>> euler005(20)
    232792560
    '''
    start = 1
    multiply = range(2, n+1)  # steps through each integer in the range.
    for i in multiply:
        if start % i != 0: 
            try:
                start = start * list(divisors(i))[1]  # multiplies by the smallest factor
            except IndexError:
                start = start * i  # if is prime, multiply by that number
    return start
