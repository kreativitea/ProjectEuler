def readfile(filename):
    ''' Reads a file in the solution data directory.
    Returns a file object. '''
    f = open('data\{}'.format(filename))
    return f

def printdoc(fn):
    ''' Prints the docstring of a function without the test cases. '''
    fn_name = fn.__name__[5:].strip('0')
    docstring = iter(fn.__doc__.split('\n'))
    p_name = docstring.next()

    print 'Project Euler Problem {}: {}'.format(fn_name, p_name)

    no_tests = []
    for docline in docstring:
        if not docline.strip().startswith('>>>'):
            print docline
        else:
            break

def matrix(f, fn):
    ''' Converts a matrix of space-seperated numbers into a list of lists.
    fn is the function that you call on each item in the matrix (e.g. int) '''
    return [[fn(i) for i in j] for j in [i.split() for i in f]]