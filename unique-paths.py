def solution(m, n):
  """
  A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

  The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

  How many possible unique paths are there?


  possible move right and down
  first row cell= 1
  first col cell = 1 
        right
  left  _^_^_  <=== #(right) + #(left)



  """
  dp = [[1 for _ in n] for _ in m]

  for row in range(1, m):
    for col in range(1, n):
      dp[row][col] = dp[row - 1][col] + dp[row][col - 1]

  return dp[row - 1][col - 1]
