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
