from operator import mul


def euler011(n, grid):
    ''' Largest product in a grid

    In the 20*20 grid below, four numbers along a diagonal line have been marked in red.

    The product of these numbers is 26 * 63 * 78 * 14 = 1788696.

    What is the greatest product of four adjacent numbers in any direction (up, down, left, right, or diagonally) 
    in the 20 * 20 grid? 
    
    >>> from eutility.fileops import readfile
    >>> from eutility.fileops import matrix 
    >>> with readfile('euler011.txt') as f:
    >>>     n = int(f.next())
    >>>     grid = matrix(f, int)
    >>> euler011(4, grid)
    70600674 
    '''
    results = []
    # verticals
    for i in range(len(grid) - n+1):
        for j in range(len(grid[0])):
            [grid[i+k][j] for k in range(n)]
            results.append(reduce(mul, [grid[i+k][j] for k in range(n)]))
        
    # horizontals
    for i in range(len(grid)):
        for j in range(len(grid[0]) - n+1):
            [grid[i][j+k] for k in range(n)]
            results.append(reduce(mul, [grid[i][j+k] for k in range(n)]))
    
    # diagonal
    for i in range(len(grid) - n+1):
        for j in range(len(grid[0]) - n+1):
            [grid[i+k][j+k] for k in range(n)]
            results.append(reduce(mul, [grid[i+k][j+k] for k in range(n)]))

    # reverse diagonals
    for i in range(n-1, len(grid)):
        for j in range(len(grid[0]) - n+1):
            results.append(reduce(mul, [grid[i-k][j+k] for k in range(n)]))

    return max(results)
