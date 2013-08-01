from eutility.eutility import timer
from eutility.fileops import readfile
from eutility.fileops import printdoc
from eutility.fileops import matrix


# This is a list of solved problems.  
# the euler000 function is the generic version of the problem.
# the problem000 function takes no arguments,
# and solves the problems with the inputs defined on the website.


def problem001():
    from problems.euler001 import euler001
    printdoc(euler001)

    with readfile('euler001.txt') as f:
        limit = int(f.next())
        ns = [int(i) for i in f]

    with timer():
        return euler001(ns, limit)


def problem002():
    from problems.euler002 import euler002
    printdoc(euler002)

    with readfile('euler002.txt') as f:
        limit = int(f.next())

    with timer():
        return euler002(limit)


def problem003():
    from problems.euler003 import euler003
    printdoc(euler003)

    with readfile('euler003.txt') as f:
        limit = int(f.next())
    
    with timer():
        return euler003(limit)


def problem004():
    from problems.euler004 import euler004
    printdoc(euler004)

    with readfile('euler004.txt') as f:
        n = int(f.next())
    
    with timer():
        return euler004(n)


def problem005():
    from problems.euler005 import euler005
    printdoc(euler005)

    with readfile('euler005.txt') as f:
        n = int(f.next())

    with timer():
        return euler005(n)


def problem006():
    from problems.euler006 import euler006
    printdoc(euler006)

    with readfile('euler006.txt') as f:
        n = int(f.next())

    with timer():
        return euler006(n)


def problem007():
    from problems.euler007 import euler007
    printdoc(euler007)

    with readfile('euler007.txt') as f:
        n = int(f.next())

    with timer():
        return euler007(n)


def problem008():
    from problems.euler008 import euler008
    printdoc(euler008)

    with readfile('euler008.txt') as f:
        n = int(f.next())
        data = f.next()

    with timer():
        return euler008(n, data)


def problem009():
    from problems.euler009 import euler009
    printdoc(euler009)

    with timer():
        return euler009()


def problem010():
    from problems.euler010 import euler010
    printdoc(euler010)

    with readfile('euler010.txt') as f:
        limit = int(f.next())

    with timer():
        return euler010(limit)
   

def problem011():
    from problems.euler011 import euler011
    printdoc(euler011)

    with readfile('euler011.txt') as f:
        n = int(f.next())
        grid = matrix(f, int)

    with timer():
        return euler011(n, grid)


def problem012():
    from problems.euler012 import euler012
    printdoc(euler012)

    with readfile('euler012.txt') as f:
        n = int(f.next())

    with timer():
        return euler012(n)


def problem013():
    from problems.euler013 import euler013
    printdoc(euler013)

    with readfile('euler013.txt') as f:
        n = int(f.next())
        data = [int(i) for i in f]
        return euler013(n, data)


def problem014():
    from problems.euler014 import euler014
    printdoc(euler014)

    with readfile('euler014.txt') as f:
        limit = int(f.next())

    with timer():
        return euler014(limit)


def problem015():
    from problems.euler015 import euler015
    printdoc(euler015)
    
    with readfile('euler015.txt') as f:
        n = int(f.next())

    with timer():
        return euler015(n)


def problem016():
    from problems.euler016 import euler016
    printdoc(euler016)

    with readfile('euler016.txt') as f:
        exp = int(f.next())

    with timer():
        return euler016(exp)


def problem017():
    from problems.euler017 import euler017
    printdoc(euler017)

    with readfile('euler017.txt') as f:
        start = int(f.next())
        end = int(f.next())

    with timer():
        return euler017(start, end)


def problem018():
    from problems.euler018 import euler018
    printdoc(euler018)

    with readfile('euler018.txt') as f:
        triangle = matrix(f, int)

    with timer():
        return euler018(triangle)


def problem019():
    from problems.euler019 import euler019
    printdoc(euler019)

    with readfile('euler019.txt') as f:
        dates = matrix(f, int)

    with timer():
        return euler019(dates[0], dates[1])


def problem020():
    from problems.euler020 import euler020
    printdoc(euler020)

    with readfile('euler020.txt') as f:
        n = int(f.next())

    with timer():
        return euler020(n)


def problem021():
    from problems.euler021 import euler021
    printdoc(euler021)

    with readfile('euler021.txt') as f:
        limit = int(f.next())

    with timer():
        return euler021(limit)


if __name__ == "__main__":
    _problems = [fn for fn in dir() if fn.startswith('problem')]
    while True:
        p = raw_input("Which problem would you like to run? (Type 'exit' to exit): ").strip()
        
        # exit condition
        if p == 'exit':
            break
        
        # run all problems
        elif p == 'all':
            for p in _problems:
                print '\n'
                eval('{}()'.format(p))
        
        else:
            # pick a single problem to run
            p = 'problem{}'.format(p.zfill(3))
            if p in _problems:
                print '\n'
                eval('{}()'.format(p))
                print '\n'
            else:
                print 'This problem ({}) has not yet been added to the solutions list.'.format(p)
                print 'Please choose again.\n'
    