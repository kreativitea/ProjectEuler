from eutility.eutility import timer
from eutility.fileops import readfile
from eutility.fileops import printdoc


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