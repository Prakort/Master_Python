def solution(nums):
  n = len(nums)
  # O(1) space max integer is 100
  # 101 covers 100 int, 102 covers 0 index since we use the element as the index
  # this is counter
  counter = [0] * 102
  res = [0] * n
  # increment counter
  for i in nums:
    counter[i+1] += 1
    
  # add the occurrence of smallest to the largest
# we do this to avoid sorting since we use element as index, it is sorted in the counter list
  for i in range(1,len(counter)):
    counter[i] += counter[i-1]
  
  # get count in the result list
  for i in range(n):
    res[i] = counter[nums[i]]
  
  return res
          
