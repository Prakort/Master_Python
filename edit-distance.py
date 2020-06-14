def minDistance(word1: str, word2: str) -> int:
  """
  Method: DP 

  using 2D table to store the min operation to convert word1 to word2 
  we want to check the left cell, bottom cell, left_bottom cell
  current cell = 1 + min(left,bottom,left_bottom)
  add 1 is because we are currently at a new char, the substring increase by 1
  - Fact, we add initiale value to check index as value of the cost to convert to another substring from empty/nothing to up to that substring
  - Notice that converting one char to a different one costs 1 
  but if the they are the same, it cost 0 because they are at the same index we need it, no need to replace or edit.
  - Notice that each computation is done based on the previous computation:
  as the very first char to another to string, we use the initiale value to compute the conversion. The same idea for the next char, in both index are the same, we dont need to add 1 

  """
  n = len(word1)
  m = len(word2)

  # prepare the 2D list
  dp = [[0 for i in range(m + 1)] for j in range(n + 1)]

  # add value for the index in each row
  for row in range(n + 1):
    dp[row][0] = row
  # add value for the index in each col
  for col in range(m + 1):
    dp[0][col] = col
    
  # start from index 1, since index 0 is already stored the default cost value
  # index is 1 offset, compare to the index in the string 
  # since we used index 0 for the cost value, keep that in mind
  for row in range(1, n + 1):
    for col in range(1, m + 1):
      
      # from the left value to the right add 1 ( means the same as from that index converting from substring of w1 to w2 or w2 to w1, costs the same)
      left = dp[row - 1][col] + 1
      # from the bottom to the the top add 1
      down = dp[row][col -1] + 1
      # this is the previous computation up to this substring cost
      left_down = dp[row -1][col -1] + 1
      # as index is 1 offset, word1[row -1] and word2[col -1]
      # are actually the current chars, not the previous computation
      # if they are the same, there is no cost to edit
      # else add 1 to the previous cost
      if word1[row -1] != word2[col -1]:
        dp[row][col] = min(left, left_down, down)
      # update the cell with the min
      else:
        dp[row][col] = dp[row - 1][col -1]
     
      
  # the last cell is the min cost to convert
  return dp[row][col]
