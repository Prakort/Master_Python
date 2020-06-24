""" 
Given a non-empty array containing only positive integers,
find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

Input: [1, 5, 11, 5]
Output: true

[11] = 11
[1,5,5] = 11
"""
def dp1D(nums):
  total = sum(nums)
  if total % 2 == 1:
    return False 
  n = len(nums) + 1
  half = total // 2 + 1

  grid = [False for _ in range(half)]
  grid[0] = True 

  for i in range(1, n):
    for j in reversed(range(half)):
      # if sum J >= nums, find the complement of in the prev row target 5 - cur nums(2) = 3
      # if grid[3] = True, {subset} sum = 5
      # we are doing reversed to preverse the previous right values because we need them
      if j >= nums[i - 1]:
        grid[j] = grid[j-1] or grid[j - nums[i-1]]

  return grid[-1]
def dp2D(nums):
  total = sum(nums)
  if total % 2 == 1:
    return False 
  n = len(nums) + 1
  half = total // 2 + 1

  grid = [[False for _ in range(half)] for _ in range(n)]
  grid[0][0] = True 

  for i in range(1, n):
    for j in range(half):
      # if sum J >= nums, find the complement of in the prev row target 5 - cur nums(2) = 3
      # if grid[i-1][3] = True, {subset} sum = 5
      if j >= nums[i - 1]:
        grid[i][j] = grid[i-1][j] or grid[i-1][j - nums[i-1]]
  return grid[-1][-1]

def memorization(nums):
  total = sum(nums)
  if total % 2 == 1:
    return False 
  
  half = total // 2 + 1

  memo = set([0])

  for n in nums:
    copies = copy.deepcopy(memo)
    for copy in copies:
      memo.add(copy + n)

  return half in memo

