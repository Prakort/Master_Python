def solution(text, pattern):
  """
  
  pattern: a*
  text: a
  result: YES, 

  pattern: ab*
  text: a
  result: YES
  Why? we check 'a' against '*' since it's '*' -> 'b' >= 0 
  then we check 'a' against 'a' dp[i][j] = d[i][j-2] 
  in this case 'a' == 'a' if not return False

  pattern: ab* or a.b*
  text: xb follow above step but '.' matches any char or 'x' == 'x'
  we just ingore 'b*' and 'b', check the previous char with 'b*' and 'b'
  so a vs x, a. vs x
  """
  
  S = ' '+ text
  P = ' '+ pattern
  len_s = len(S)
  len_p = len(P)
  
  dp = [[False for _ in P] for _ in S]
  dp[0][0] = True
  # take care of a*
  #         True True
  
  for i in range(1, len_p):
    if P[i] == '*':
      dp[0][i] = dp[0][i-2]
      
  for row in range(1, len_s):
    for col in range(1, len_p):
      # if a char meet '.', check the previous computation the inner char
      if P[col] in {S[row], "."}:
        dp[row][col] = dp[row-1][col-1]
      # if a char meet '*'
      # case 1, check pattern: xb*, str: x consider b* could be 0 occurrence, we check x vs x 
      # case 2, pattern ab* , str ab, if a char before '*' == a char in text or '.', we ignore them both, only check previous pattern since we match,
      # check a and a that dp[row-1][col]
      elif P[col] == '*':
        dp[row][col] = dp[row][col-2] or (dp[row-1][col] and P[col-1] in {S[row], '.'})

  return dp[-1][-1]
