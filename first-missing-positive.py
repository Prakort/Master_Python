def solution(nums):
  """
  the first missing int [1,n+1]
  we are checking if i + 0 == nums[i]
  if it not, we will swap the 
  nums[i] = nums[nums[i] - 1]
  nums[nums[i] -1] = nums[i]
  eg. [9,8,6,7,5,4,3,2,1]
  nums [1, 8, 6, 7, 5, 4, 3, 2, 9] index 0
  nums [1, 2, 6, 7, 5, 4, 3, 8, 9] index 1
  nums [1, 2, 4, 7, 5, 6, 3, 8, 9] index 2
  nums [1, 2, 7, 4, 5, 6, 3, 8, 9] index 2
  nums [1, 2, 3, 4, 5, 6, 7, 8, 9] index 2
  
  in the second loop
  we find the i + 1 != nums[i] return that i + 1 is the first missing int
  """
  n = len(nums)
  for i in range(n):
    # we want to swap the element to its correct index i + 1
    while 0 < i <= n and i + 1  != nums[i] and nums[nums[i] -1] != nums[i]:
      nums[nums[i] -1], nums[i] = nums[i], nums[nums[i] -1]


  for i in range(n):
    if i + 1 != nums[i]:
      return i + 1


  return n + 1
