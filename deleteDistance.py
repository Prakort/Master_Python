def deletion_distance(str1, str2):
  
  # str1 as col
  # str2 as row
  l1 = len(str1)
  l2 = len(str2)
  
  dp = [[0 for i in range(l1+1)] for i in range(l2+1)]
  
  for row in range(l2+1): # 
    dp[row][0] = row
    
    # row = len2
    # col = len1
    
  for col in range(l1+1): # col [0,4)
    dp[0][col] = col
    
  for i in range(1, l2+1):
    for j in range(1, l1+1):
      if str1[j-1] == str2[i-1]:
        dp[i][j] = dp[i-1][j-1]
      else:
        delete1 = dp[i-1][j] + 1
        delete2 = dp[i][j-1] + 1
        deleteBoth = dp[i-1][j-1] + 2
        dp[i][j] = min(delete1, delete2, deleteBoth)
        
  return dp[l2][l1]
  
  
print(deletion_distance("dog", "frog"))
