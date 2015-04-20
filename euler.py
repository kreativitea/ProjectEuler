from eutility.eutility import timer
from eutility.fileops import data
from eutility.fileops import printdoc
from eutility.fileops import matrix
from eutility.fileops import readcsv


# This is a list of solved problems.
# the euler000 function is the generic version of the problem.
# the problem000 function takes no arguments,
# and solves the problems with the inputs defined on the website.


def problem001():
    from problems.euler001 import euler001
    printdoc(euler001)

    with data('euler001.txt') as f:
        limit = int(f.next())
        ns = [int(i) for i in f]

    with timer():
        return euler001(ns, limit)


def problem002():
    from problems.euler002 import euler002
    printdoc(euler002)

    with data('euler002.txt') as f:
        limit = int(f.next())

    with timer():
        return euler002(limit)


def problem003():
    from problems.euler003 import euler003
    printdoc(euler003)

    with data('euler003.txt') as f:
        limit = int(f.next())

    with timer():
        return euler003(limit)


def problem004():
    from problems.euler004 import euler004
    printdoc(euler004)

    with data('euler004.txt') as f:
        n = int(f.next())

    with timer():
        return euler004(n)


def problem005():
    from problems.euler005 import euler005
    printdoc(euler005)

    with data('euler005.txt') as f:
        n = int(f.next())

    with timer():
        return euler005(n)


def problem006():
    from problems.euler006 import euler006
    printdoc(euler006)

    with data('euler006.txt') as f:
        n = int(f.next())

    with timer():
        return euler006(n)


def problem007():
    from problems.euler007 import euler007
    printdoc(euler007)

    with data('euler007.txt') as f:
        n = int(f.next())

    with timer():
        return euler007(n)


def problem008():
    from problems.euler008 import euler008
    printdoc(euler008)

    with data('euler008.txt') as f:
        n = int(f.next())
        number = f.next()

    with timer():
        return euler008(n, number)


def problem009():
    from problems.euler009 import euler009
    printdoc(euler009)

    with timer():
        return euler009()


def problem010():
    from problems.euler010 import euler010
    printdoc(euler010)

    with data('euler010.txt') as f:
        limit = int(f.next())

    with timer():
        return euler010(limit)


def problem011():
    from problems.euler011 import euler011
    printdoc(euler011)

    with data('euler011.txt') as f:
        n = int(f.next())
        grid = matrix(f, int)

    with timer():
        return euler011(n, grid)


def problem012():
    from problems.euler012 import euler012
    printdoc(euler012)

    with data('euler012.txt') as f:
        n = int(f.next())

    with timer():
        return euler012(n)


def problem013():
    from problems.euler013 import euler013
    printdoc(euler013)

    with data('euler013.txt') as f:
        n = int(f.next())
        ns = [int(i) for i in f]
        return euler013(n, ns)


def problem014():
    from problems.euler014 import euler014
    printdoc(euler014)

    with data('euler014.txt') as f:
        limit = int(f.next())

    with timer():
        return euler014(limit)


def problem015():
    from problems.euler015 import euler015
    printdoc(euler015)

    with data('euler015.txt') as f:
        n = int(f.next())

    with timer():
        return euler015(n)


def problem016():
    from problems.euler016 import euler016
    printdoc(euler016)

    with data('euler016.txt') as f:
        exp = int(f.next())

    with timer():
        return euler016(exp)


def problem017():
    from problems.euler017 import euler017
    printdoc(euler017)

    with data('euler017.txt') as f:
        start = int(f.next())
        end = int(f.next())

    with timer():
        return euler017(start, end)


def problem018():
    from problems.euler018 import euler018
    printdoc(euler018)

    with data('euler018.txt') as f:
        triangle = matrix(f, int)

    with timer():
        return euler018(triangle)


def problem019():
    from problems.euler019 import euler019
    printdoc(euler019)

    with data('euler019.txt') as f:
        dates = matrix(f, int)

    with timer():
        return euler019(dates[0], dates[1])


def problem020():
    from problems.euler020 import euler020
    printdoc(euler020)

    with data('euler020.txt') as f:
        n = int(f.next())

    with timer():
        return euler020(n)


def problem021():
    from problems.euler021 import euler021
    printdoc(euler021)

    with data('euler021.txt') as f:
        limit = int(f.next())

    with timer():
        return euler021(limit)


def problem022():
    from problems.euler022 import euler022
    printdoc(euler022)

    with data('euler022.txt') as f:
        filedata = readcsv(f.next(), fn=lambda x: x.strip('"'))

    with timer():
        return euler022(filedata)


def problem023():
    from problems.euler023 import euler023
    printdoc(euler023)

    with data('euler023.txt') as f:
        limit = int(f.next())

    with timer():
        return euler023(limit)


def problem024():
    from problems.euler024 import euler024
    printdoc(euler024)

    with data('euler024.txt') as f:
        n = int(f.next())
        digits = int(f.next())

    with timer():
        return euler024(n, digits)


def problem025():
    from problems.euler025 import euler025
    printdoc(euler025)

    with data('euler025.txt') as f:
        length = int(f.next())

    with timer():
        return euler025(length)


def problem026():
    from problems.euler026 import euler026
    printdoc(euler026)

    with data('euler026.txt') as f:
        maxn = int(f.next())

    with timer():
        return euler026(maxn)


def problem027():
    from problems.euler027 import euler027
    printdoc(euler027)

    with data('euler027.txt') as f:
        limit = int(f.next())

    with timer():
        return euler027(limit)


def problem028():
    from problems.euler028 import euler028
    printdoc(euler028)

    with data('euler028.txt') as f:
        diagonal = int(f.next())

    with timer():
        return euler028(diagonal)


def problem029():
    from problems.euler029 import euler029
    printdoc(euler029)

    with data('euler029.txt') as f:
        a = int(f.next())
        b = int(f.next())

    with timer():
        return euler029(a, b)


def problem030():
    from problems.euler030 import euler030
    printdoc(euler030)

    with data('euler030.txt') as f:
        power = int(f.next())

    with timer():
        return euler030(power)


def problem035():
    from problems.euler035 import euler035
    printdoc(euler035)

    with data('euler035.txt') as f:
        limit = int(f.next())

    with timer():
        return euler035(limit)

def problem036():
    from problems.euler036 import euler036
    printdoc(euler036)

    with data('euler036.txt') as f:
        limit = int(f.next())

    with timer():
        return euler036(limit)


def problem037():
    from problems.euler037 import euler037
    printdoc(euler037)

    with data('euler037.txt') as f:
        n = int(f.next())

    with timer():
        return euler037(n)


if __name__ == "__main__":
    _problems = [fn for fn in dir() if fn.startswith('problem')]
    while True:
        p = raw_input("Which problem would you like to run? (Type 'help' for help): ").strip()

        # exit condition
        if p == 'exit':
            break

        elif p == 'list':
            print _problems

        elif p == 'help':
            print ('\n'
                   'exit:  exits the program.\n'
                   'list:  lists all problems.\n'
                   'all:   runs all problems.\n')

        # run all problems
        elif p == 'all':
            for p in _problems:
                print '\n'
                eval('{}()'.format(p))

        else:
            # account for format '13' or 'problem013'
            if p in _problems:
                prob = p
            else:
                prob = 'problem{}'.format(p.zfill(3))

            # run the problem itself
            if prob in _problems:
                print '\n'
                eval('{}()'.format(prob))
                print '\n'

            else:
                try:
                    int(p)
                    print 'This problem ({}) has not yet been added to the solutions list.'.format(prob)
                    print 'Please choose again.\n'
                except:
                    print "I'm sorry, '{}' is not a valid command.  Please try again.".format(p)
