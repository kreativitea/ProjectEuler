def euler015(n):
    ''' Lattice paths
    
    Starting in the top left corner of a 2 x 2 grid, there are 6 routes 
    (without backtracking) to the bottom right corner.

    How many routes are there through a 20 x 20 grid? '''
    matrix = [[0 for i in xrange(n+1)] for i in xrange(n+1)]


    for i in xrange(n+1):
        for j in xrange(n+1):
            if not i:
                matrix[i][j] = 1
            else:
                matrix[i][j] = matrix[i-1][j] + matrix[i][j-1]

    return matrix[-1][-1]
