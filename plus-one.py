def solution(nums):

  for i in range(len(nums)):
    if nums[i] < 9:
      nums[i] +=1
      return 
    nums[i] = 0

  return [1] + nums
