def solution(grid):
  # we want to find number of island 
  # if they have the same shape, we count as one
  # how to recognize the shape
  # r1 - r1 == r1' - r1'
  # r2 - r1 == r2' - r2'
  # c1 - c1 == c1' - c1'
  # if they have the same shape, the diff between their coordinates is the same

  res = set()
  rows = len(grid)
  cols = len(grid[0])
  visited = [[False for _ in range(cols)] for _ in range(rows)]
  for i in range(rows):
    for j in range(cols):
      if grid[i][j] == 1 and not visited:
        shape = dfs(grid, rows, cols, i, j, i, j, visited, set())
        # set of sets, inner set has to be frozenset to be hashable
        res.append(frozenset(shape))

  return len(res)


def dfs(grid, rows, cols, r, c, start_r, start_c, visited, shape):
  if 0 <= r < rows and 0 <= c < cols and not visited and grid[r][c] == 1:
    shape = str(r - start_r) + ':' + str(c - start_c)
    visited = True
    for i, j in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
      dfs(grid, rows, cols, i, j, start_r, start_c, visited, shape)

    return shape

