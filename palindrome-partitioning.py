"""
"aab"
["a","a","b"]
["aa","b"]
check every substring of all partitions

Fact: every char is a palindrome -> ["a","a","b"] is one of the answer
Fact: we have to check all substring as follow:
aab, we iterator i = 0 to i = n - 1

when a substring at 0-i is a palindrome, we will perform 
dfs onto next index which i + 1 to evaluate all possible 
substring from i+1 to n
aabaa 
i = 0 loop 0 to n
  found at s[:i] is palidrome
    find other substring from i + 1 to n
      i+1, i+2
      i+1, i+2 i+3
      this keep branching off if there is a palindrome substring
  
runtime: O(2^n) we will check all the combination of every character of string with length n, we perform to check palindrome, for all combination O(n(2^n)) which O(2^n)
space: O(n), we have to to place function on stacks, 
the height number of stacks is n length of the char
since we have to check every char. The deepest recursion is N
"""

def solution(s):
  res = []
  dfs(s, 0, [], res)
  return res

def dfs(s, start, path, res):
  #base case 
  if start == len(s):
    res.append(path)
    return 

  for i in range(start, len(s)):
    if isPalindrome(s[start:i+1]):
      ans = path[:]
      ans.append(s[start:i+1])
      dfs(s, i+1, ans, res)

def isPalindrome(s):
  r = len(s) - 1
  l = 0
  while l < r < len(s):
    if s[r] != s[l]:
      return False 
    l +=1
    r -=1

  return True 



