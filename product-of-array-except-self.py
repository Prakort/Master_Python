def solution(nums):

  length = len(nums)
  output = [1] * length
  right = [1] * length 
  left = [1] * length 

  for i in range(1, length):
    left[i] = left[i - 1] * nums[i - 1]

  for i in reversed(range(length)):
    right[i] = right[i + 1] * nums[i + 1]

  for i in range(length):
    output[i] = left[i] + right[i]

  return output 
