def validPalindrome(s):
  for i in range(len(s)//2):
    if s[i] != s[~i]:
      right = len(s) -1 -i
      return isPalindrome(s, i+1, right) or isPalindrome(s, i, right - 1)
  return True 

def isPalindrome(s, left, right):
  while left <= right:
    if s[left] != s[right]:
      return False 
    left += 1
    right -= 1

  return True

def solution2(s):
  for i in range(len(s)//2):
    end = len(s) -1 - i
    if s[i] != s[end]:
      return isPal(s[i+1:end+1]) or isPal(s[i:end])
def isPal(s):
  return s[:] == s[::-1]
