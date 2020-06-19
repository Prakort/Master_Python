def solution(grid):
  """ 
  Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

  Note: You can only move either down or right at any point in time.

  Input:
  [
    [1,3,1],
    [1,5,1],
    [4,2,1]
  ]
  Output: 7
  Explanation: Because the path 1→3→1→1→1 minimizes the sum.

  runtime: O(mxn)
  space: O(mxn)

  """
  m = len(grid)
  n = len(grid[0])

  dp = copy.deepcopy(grid)

  for row in range(m):
    for col in range(n):
      if row > 0 and col > 0:
        dp[row][col] += min(dp[row-1][col], row[row][col-1])
      elif row > 0:
        dp[row][col] += dp[row-1][col]
      elif col > 0:
        dp[row][col] += dp[row][col-1]
  
  return dp[m-1][n-1]

def solution2(grid):
  """ 
  runtime: O(mxn)
  space: O(1)

  """
  m = len(grid)
  n = len(grid[0])

  for row in range(m):
    for col in range(n):
      if row > 0 and col > 0:
        grid[row][col] += min(grid[row-1][col], grid[row][col-1])
      elif row > 0:
        grid[row][col] += grid[row-1][col]
      elif col > 0:
        grid[row][col] += grid[row][col-1]
  
  return grid[m-1][n-1]

