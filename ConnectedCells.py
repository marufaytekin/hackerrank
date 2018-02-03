"""
Consider a matrix with  rows and  columns, where each cell contains either a 0
or a 1 and any cell containing a  is called a filled cell. Two cells are said
to be connected if they are adjacent to each other horizontally, vertically,
or diagonally; in other words, cell [i][j] is connected to cells
[i-1][j-1], [i-1][j], [i-1][j+1], [i][j-1], [i][j+1], [i+1][j-1],[i+1][j],
and [i+1][j+1] provided that the location exists in the matrix for that [i][j].

If one or more filled cells are also connected, they form a region. Note that
each cell in a region is connected to at least one other cell in the region but
is not necessarily directly connected to all the other cells in the region.

Task:
Given an  n x m matrix, find and print the number of cells in the largest region in
the matrix. Note that there may be more than one region in the matrix.
"""


def dfs(grid, visited, i, j):
    m = len(grid)
    n = len(grid[0])
    if i < 0 or j < 0 or i > m - 1 or j > n - 1 or grid[i][j] == 0 or visited[i][j]:
        return 0
    else:
        visited[i][j] = True
        return 1 + \
               dfs(grid, visited, i - 1, j - 1) + \
               dfs(grid, visited, i, j - 1) + \
               dfs(grid, visited, i + 1, j - 1) + \
               dfs(grid, visited, i - 1, j) + \
               dfs(grid, visited, i + 1, j) + \
               dfs(grid, visited, i - 1, j + 1) + \
               dfs(grid, visited, i, j + 1) + \
               dfs(grid, visited, i + 1, j + 1)


def calculate_largest_region(grid):
    m = len(grid)
    n = len(grid[0])
    result = [[0 for elem in range(n)] for elem in range(m)]
    visited = [[False for elem in range(n)] for elem in range(m)]

    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                result[i][j] = dfs(grid, visited, i, j)
    return max(result[i][j] for i in range(m) for j in range(n))


_grid = [[1, 1, 0, 0], [0, 1, 1, 0], [0, 0, 1, 0], [1, 0, 0, 0]]
_grid2 = [[0, 0, 0, 1], [1, 1, 0, 1], [0, 1, 1, 0], [0, 1, 0, 0]]

print calculate_largest_region(_grid)
print calculate_largest_region(_grid2)
