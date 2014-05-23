import time
import math

from itertools import izip
from itertools import count
from itertools import chain
from itertools import izip_longest
from collections import deque


class timer():
    def __init__(self):
        self.start = None
        self.runtime = None
    def __enter__(self):
        self.start = time.time()
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.runtime = time.time() - self.start
        print 'This code returned a result in {0:.6f} seconds.'.format(self.runtime)


def memodict(f):
    ''' Memoization decorator for a function taking a single argument '''
    class memodict(dict):
        def __missing__(self, key):
            ret = self[key] = f(key)
            return ret 
    return memodict().__getitem__


def memoize(f):
    ''' Memoization decorator for a function taking one or more arguments. '''
    class memodict(dict):
        def __getitem__(self, *key):
            return dict.__getitem__(self, key)

        def __missing__(self, key):
            ret = self[key] = f(*key)
            return ret

    return memodict().__getitem__


def lcs(a, b=None):
    ''' Longest common substring algorithm. '''
    if not b:
        # finds longest substring within itself
        b = a
        M = [[0 for i in xrange(len(a) + 1)] for j in xrange(len(b) + 1)]
        max_i, max_val = 0, 0
        for i, va in enumerate(a):
            for j, vb in enumerate(b):
                if (va == vb) and (i != j):
                    val = M[i-1][j-1] + 1
                    M[i][j] = val
                    if val > max_val:
                        max_i, max_val = i, val
    else:
        # normal lcs between two strings
        M = [[0 for i in xrange(len(a) + 1)] for j in xrange(len(b) + 1)]
        max_i, max_val = 0, 0
        for i, va in enumerate(a):
            for j, vb in enumerate(b):
                if (va == vb):
                    val = M[i-1][j-1] + 1
                    M[i][j] = val
                    if val > max_val:
                        max_i, max_val = i, val
    return a[max_i-max_val+1:max_i+1]


def grouper(iterable, n, fillvalue=None):
    "Collect data into fixed-length chunks or blocks"
    # grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx
    args = [iter(iterable)] * n
    return izip_longest(fillvalue=fillvalue, *args)


def short_grouper(iterable, n):
    "Collect data into fixed-length chunks or blocks"
    # grouper('ABCDEFG', 3, 'x') --> ABC DEF
    args = [iter(iterable)] * n
    return izip(*args)


class Biggest(object):
    def __init__(self, value=0, data=None):
        self.value = value
        self.data = data

    def set(self, value, data=None):
        if value > self.value:
            self.data = data
            self.value = value

    def __repr__(self):
        if self.data:
            return unicode("Biggest({}, '{}')".format(self.value, self.data))
        else:
            return unicode('Biggest({})'.format(self.value))
