def removeDuplicates(nums: List[int]) -> int: 
  """
  set the tracker of the element is start
  if counter > 2, replace the element with float('inf')
  
  check the prev and curr, if they are the same,
  increment the counter else reset the counter and update the tracker to the curr element
  
  count the float('inf')
  
  
  why tracker ? it helps replacing the duplicate
  """
  n = len(nums)
  
  if not n:
    return 0
  
  start = 1
  # define the tracking element
  value = nums[0]

  for i in range(1,n):
    # check if it is a duplicate
    if nums[i] == value:
      start += 1
      
      # check the counter
      if start >= 3:
        # replace the duplicate element
        nums[i] = float('-inf')
    
    else:
      # update the tracking element
      value = nums[i]
      # reset the count
      start = 1

  # count the removing duplicate
  index = 0
  for i in range(n):
    if nums[i] != float('-inf'):
      nums[index] = nums[i]
      index += 1

  return index
