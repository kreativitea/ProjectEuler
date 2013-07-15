def readfile(filename):
    ''' Reads a file in the solution data directory.
    Returns a file object. '''
    f = open('data\{}'.format(filename))
    return f