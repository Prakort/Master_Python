def solution(n):
  """
  isBadVersion provided 
  input 1..N bad version at index i then i+1 all bad versions
  """
  for i in range(1,n):
    if isBadVersion(i):
      return i
  return n 

def solution2(n):
  # good good good bad bad bad bad bad
  # we could performs BST
  left = 1
  right = n
  while left < right:
    mid = left + (right - left) // 2
    if isBadVersion(mid):
      right = mid 
    else:
      left = mid + 1
  
  return left

