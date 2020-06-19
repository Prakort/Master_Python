def solution(nums):
  n = len(nums)
  start = 0
  end = n - 1
  res = 0

  while start < end:
    res = max(res, min(nums[start], nums[end]) * (end - start))
    if nums[start] < nums[end]:
      start += 1
    else:
      end -= 1
  return res 
