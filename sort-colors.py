def solution(nums):
  r = w = b = 0
  for i in nums:
    if i == 0:
      r += 1
    if i == 1:
      w += 1
    if i == 2:
      b += 1
    

  for i in range(len(nums)):
    if r > 0:
      nums[i] = 0
      r -= 1
    elif w > 0:
      nums[i] = 1
      w -= 1
    elif b > 0:
      nums[i] = 2
      b -= 1
      
def solution2(nums):
  n = len(nums)
  # one_index tracks next  0 position could be placed
  # but it doesn't mean that nums[one_index] is 0
  # i track current number
  one_index = i = 0
  # two_index tracks next 2 position could be placed
  two_index = n - 1
  
  while one_index < two_index and i < n:
    # find 0
    # place it in one_index where the 0 should be
    # nums[i] is 0 so swap with nums[one_index] which is not 0
    if nums[i] == 0:
      nums[i] = nums[one_index]
      nums[one_index] = 0
      one_index +=1
      index += 1
    # found 2
    # swap values where 2 should be at the end of the list
    elif nums[i] == 2:
      nums[i] = nums[end_index]
      nums[two_index] = 2
      # getting to the left
      two_index -= 1
      # not increment index
      # we do not we that nums[two_index] value
      # we have to iterate on it again
    else:
      i += 1
      
      
      
  
    