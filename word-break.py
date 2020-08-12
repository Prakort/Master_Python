def solution(s, wordList):
  n = len(s)
  given = set(wordList)

  dp = [False for _ in range(n+1)]

  for i in range(n):
    if not dp[i]:
      continue
    for j in range(i+1,n+1):
      if s[i:j] in given:
        dp[j] = True 

  return dp[-1]
