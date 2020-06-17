def solution(nums):
  # runtime O(N^2)
  # space O(1)
  start, end = 0, len(nums)

  for i in range(len(nums) - 1):
    for j in range(i + 1, len(nums)):
      if nums[j] < nums[i]:
        start = min(start, i)
        end = max(end, j)

  if end - start <= 0:
    return 0

  return end - start + 1

def solution2(nums):
  # make a copy of sorted nums
  sorted_nums = sorted(nums)
  start = end = 0

  for i in range(len(nums)):
    if nums[i] != sorted_nums[i]:
      start = i
      break 

  for i in range(len(nums)):
    if nums[~i] != sorted_nums[~i]:
      end = len(nums) + ~i
      break
    
  if end - start <= 0:
    return 0

  return end - start + 1
