from eutility.fileops import readfile
from eutility.eutility import time_execution

def problem001():
    from problems.euler001 import euler001
    f = readfile('euler001.txt')
    limit = int(f.next())
    ns = [int(i) for i in f]
    print euler001(ns, limit)

def problem002():
    from problems.euler002 import euler002
    f = readfile('euler002.txt')
    limit = int(f.next())
    print euler002(limit)

