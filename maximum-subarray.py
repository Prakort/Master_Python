def solution(nums):
  """
  [-2,1,-3,4,-1,2,1,-5,4]
  
  Method: Kadane's Algo
  i = 0 current sub array for the first time is [-2] 
  i = 1 we have two choice [-2,1] and [1] sub arrays
  i = 3 we have two choice [max([-2,1],[1]),-3] and [-3] 
  each index we have local maximum between prev subarray and current element
  if prev subarray + current element is greater than current element 
  that means, we have to consider the continue prev subarray 
  otherwise, current element is greater, we start a new subarray from current element 
  1 element is a sub array too
  
  
  """
  if len(nums) == 1:
      return nums[0]
  cur = ans = nums[0]
  for i in range(1, len(nums)):
      # update local sub array: new sum = (previous subarray + element) vs (element)
      if nums[i] > cur + nums[i]:
          # start/pick a new subarray
          cur = nums[i]
      else:
          # continue the previous subarray add current element in
          cur = cur + nums[i]
      # max global
      ans = max(ans, cur)
      
  return ans
