import itertools
import time
import math


class timer():
    def __init__(self):
        self.start = None
        self.runtime = None

    def __enter__(self):
        self.start = time.clock()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.runtime = time.clock() - self.start
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


