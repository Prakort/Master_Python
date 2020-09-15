class Solution():
  """ 
  Ideas:
  - get the minimum edit distance using dp
  - find at the current i,j pair where previous row and previous col 
  - example
  - w1: AB -> w2: ABC
  - change AB to ABC cost is 1 
  - we have to look at w1: A -> ABC cost is 2
  - we have to look at w2: AB -> AB cost is 0
  """
  def minimalDistance(self, word1, word2):
    
    n1 = len(word1)
    n2 = len(word2)

    # if n1 == 0:
    #   return n2
    # if n2 == 0:
    #   return n1
    # if word1 == word2:
    #   return 0

    dp = [[0 for i in range(n2+1)] for i in range(n1+1)]

    for row in range(n1+1):
      dp[row][0] = 0

    for col in range(n2+1):
      dp[0][col] = col 

    for i in range(1, n1+1):
      for j in range(1, n2+1):
        if word1[i-1] == word2 [j-1]:
          dp[i][j] = dp[i-1][j-1]
        else: 
          dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1],dp[i-1][j-1])


    i = j = 0
    res = []

    while i < n1 and j < n2:
      if word1[i] == word2[j]:
        res.append(word1[i])
        i += 1
        j += 1
      else:
        #logic source[:i] to target[:j]
        # we want to tranform s[:i] to target[:j] 
        # if dp[i][j-1] left cell, is big that mean we have to remove the char inorder to get the target[:j]
        if dp[i+2][j+1] <=  dp[i+1][j+2] :
          res.append(str('-' + word1[i]))
          i += 1
        else:
        # else dp[i-1][j] is greater than mean the target[:j] is longer and need to add char
          res.append('+' + word2[j])
          j += 1

    while j < n2:
      res.append('+' + word2[j])
      j += 1

    print("total dist: ", dp[-1][-1])
    print("result 1", res)

  def second(self, word1, word2):
    
    n1 = len(word1)
    n2 = len(word2)



    dp = [[0 for i in range(n2+1)] for i in range(n1+1)]
    for row in range(n1):
      dp[row][n2] = n1 - row
    for col in range(n2):
      dp[n1][col] = n2 - col 

    for i in reversed(range(n1)):
      for j in reversed(range(n2)):
        if word1[i-1] == word2[j-1]:
          dp[i][j] = dp[i+1][j+1]
        else:
          # print('i: ', i ,'j: ', j)
          dp[i][j] = 1 + min(dp[i+1][j], dp[i][j+1], dp[i+1][j+1])

    j = i = 0 
    res = []

    while i < n1 and j < n2: 
      if word1[i] == word2[j]:
        res.append(word1[i])
        i += 1
        j += 1
      else: 
        if dp[i+1][j] <= dp[i][j+1]:
          res.append("-" + word1[i])
          i += 1
        else: 
          res.append("+" + word2[j])
          j += 1
        

    while j < n2: 
      res.append("+" + word2[j])
      j += 1

    # for i in range(1, len(res)):
    #   if '-' in res[i] and '+' in res[i-1]:
    #     res[i-1], res[i] = res[i], res[i-1]
    print("dist is ", dp[0][0])
    print("result 2:", res)

  def third(self, word1, word2):

    n1 = len(word1)
    n2 = len(word2)

    memo = [[None for _ in range(n2)] for _ in range(n1)]

    def dp(i, j):
      if i == n1 or j == n2:
        return n2 - j

      elif memo[i][j] == None:
        if word1[i] == word2[j]:
          memo[i][j] = dp(i+1, j+1)
        else:
          memo[i][j] = 1 + min(dp(i+1, j) , dp(i , j+1))

      return memo[i][j]
    
    j = i = 0 
    res = []

    while i < n1 and j < n2: 
      if word1[i] == word2[j]:
        res.append(word1[i])
        i += 1
        j += 1
      else: 
        if dp(i+1, j) < dp(i, j+1):
          res.append("-" + word1[i])
          i += 1
        else: 
          res.append("+" + word2[j])
          j += 1
        

    while j < n2: 
      res.append("+" + word2[j])
      j += 1
    
    print("result 3:", res)
    return res




sol = Solution()

w1 = "A"
w2 = "BC"
# w1 = "CBBC"
# w2 = "CABAABBC"


w1 = "ABCD"
w2 = "ABDC"
sol.third(w1,w2)
a = ["A","B","-C","D","-E","F","+F","G","+H"]
# w1 = "HMXPHHUM"
# w2 = "HLZPLUPH"
w1 = "ABCD"
w2 = "ABDC"

w1 = "ABCDEFG"
w2 = "ABDFFGH"

w1 = "ABCD"
w2 = "ABDC"
# w1 = "GHMXGHUGXL" 
# w2 = "PPGGXHHULL"
sol.second(w1,w2)


      

