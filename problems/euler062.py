from collections import defaultdict


def euler062(digits):
    """ Cubic Permutations

    The cube, 41063625 (3453), can be permuted to produce two other cubes:

        56623104 (3843)
        66430125 (4053)

    In fact, 41063625 is the smallest cube which has exactly three permutations
    of its digits which are also cube.

    Find the smallest cube for which exactly five permutations of its digits are
    cube.

    >>> euler062(3)
    41063625L

    >>> euler062(5)
    127035954683L
    """
    # if you don't find an answer, increase the size of this value
    LIMIT = 9999

    results = defaultdict(list)
    for i in xrange(LIMIT):
        sorted_cube = ''.join(sorted(str(i ** 3)))
        results[sorted_cube].append(i)
        if len(results[sorted_cube]) == digits:
            return results[sorted_cube][0] ** 3

