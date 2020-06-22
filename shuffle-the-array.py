def solution(nums):
  n = len(nums)
  output = []

  for i in range(nums):
    output.append(nums[i])
    output.append(nums[n + i])

  return output
