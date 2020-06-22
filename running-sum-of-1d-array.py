def solution(nums):
  n = len(nums)

  if not n:
    return []
  
  for i in range(1, n):
    nums[i] += nums[i-1]

  return nums
