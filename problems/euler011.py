from eutility.fileops import readfile
from operator import mul


def problem011(adjacent):
    """ In the 20*20 grid below, four numbers along a diagonal line have been marked in red.

    The product of these numbers is 26  63  78  14 = 1788696.

    What is the greatest product of four adjacent numbers in any direction (up, down, left, right, or diagonally) 
    in the 20 * 20 grid? 
    
    >>> problem011(4)
    ... 70600674 """
    f = readfile('euler011.txt')
    
    grid = [[int(i) for i in j] for j in [i.split() for i in f]]

    results = []

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            try:
                results.append(reduce(mul, [grid[i][k] for k in (i+n for n in range(adjacent))]))
            except IndexError:
                pass

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            try:
                [grid[k][j] for k in [j+n for n in range(adjacent)]]
            except IndexError:
                pass


            i, j, [i+k for k in range(adjacent)], [j+k for k in range(adjacent)]

    return max(results)




grid = [[1, 2, 3, 4]]
grid.extend(grid)
grid.extend(grid)

for i in grid:
    print i





    zipgrid = [list(i) for i in zip(*grid)]
    reversegrid = [i[::-1] for i in grid]

    diagonalizer = [0 for i in range(len(grid))]

    diagonalgrid = [list(i) for i in zip(*[eul.insert_list(diagonalizer, i, grid[i]) for i in range(len(grid))])]
    diagonalzipgrid = [list(i) for i in zip(*[eul.insert_list(diagonalizer, i, zipgrid[i]) for i in range(len(zipgrid))])]
    
    # search should be normal matrix of as many units 
    search = grid + zipgrid + diagonalgrid + diagonalzipgrid

    max = 0
    for element in search:
        for i in range(len(element)-len_n+1):
            result = eul.multiply_list(element[i:i+len_n])
            if result > max:
                max = result
    return max
