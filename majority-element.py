def solution(nums):
  """
  Method: One Pass

  we want to find the most occurrence element that is greater than len/2 
  - use a hashmap to store the count
  - update the answer if the count is greater than len/2

  runtime: O(N) every element in the array is visited
  space: O(N) we use hasmap to store the count of every element
  """

  hm = {}
  res = float('-inf')

  for i in nums:
    hm[i] = 1 if i not in hm else (hm[i] + 1)
    
    if hm[i] > len(nums) // 2 : 
      res = i 

  return res

def solution2(nums):
  # runtime: O(nlogn)
  # space: O(1)
  nums.sort()
  return nums[len(nums)//2]
