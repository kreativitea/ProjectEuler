from itertools import count
from eutility.eutility import DefaultOrderedDict


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
    (41063625, [345, 384, 405])
    >>> euler062(4)
    (1006012008, [1002, 1020, 2001, 2010])
    >>> euler062(5)
    (127035954683, [5027, 7061, 7202, 8288, 8384])
    >>> euler062(6)
    (1000600120008, [10002, 10020, 10200, 20001, 20010, 20100])
    >>> euler062(7)
    (10569784298536, [21946, 26248, 26668, 36994, 42352, 46078, 46393])
    >>> euler062(8)
    (10314675896832, [21768, 23157, 24087, 26832, 41427, 42789, 44691, 46188])
    >>> euler062(9)
    (13465983902671, [23791, 26257, 28711, 28732, 33667, 40879, 40921, 43267, 45916])
    >>> euler062(10)
    (109867826442375, [47895, 62676, 64044, 67398, 74742, 78339, 78654, 85941, 89883, 97038])
    >>> euler062(11)
    (101729840326568, [46682, 47129, 51524, 59489, 67292, 68342, 79511, 84281, 85538, 93908, 94382])

    """
    c = count()
    results = DefaultOrderedDict(list)
    cube_length = 0

    for i in c:
        sorted_cube = ''.join(sorted(str(i ** 3)))

        if cube_length < len(sorted_cube):
            cube_length = len(sorted_cube)
            result = check_results(results, digits)
            if result:
                return result

        results[sorted_cube].append(i)


def check_results(results, digits):
    if digits == 0:
        raise ValueError("Zero digits doesn't make sense.")
    try:
        while True:
            key, value = results.popitem(last=False)
            if len(value) == digits:
                return value[0] ** 3, value
    except KeyError:
        return False
