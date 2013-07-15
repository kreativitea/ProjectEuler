from operator import mul


def euler009():
    ''' Special Pythagorean triplet

    A Pythagorean triplet is a set of three natural numbers,
    a  b  c, for which, a**2 + b**2 = c**2

    For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.

    There exists exactly one Pythagorean triplet for which a + b + c = 1000.
    Find the product abc.

    >>> euler009()
    31875000
    '''
    # observe that (8, 15, 17) is a pythagorean triplet.
    triplet = (8, 15, 17)

    # observe that sum(triplet) == 40
    # observe that 1000 / 40.0 == 25.0
    # observe that any ratio of a pythagorean triplet is also pythagorean triplet
    triplet = [25 * i for i in triplet]
    return reduce(mul, triplet)
