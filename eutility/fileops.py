def readfile(filename):
    ''' Reads a file in the solution data directory.
    Returns a file object. '''
    f = open('data\{}'.format(filename))
    return f

def printdoc(fn):
    ''' Prints the docstring of a function without the test cases. '''
    docstring = fn.__doc__.split('\n')
    no_tests = []
    for docline in docstring:
        if not docline.strip().startswith('>>>'):
            print docline
        else:
            break