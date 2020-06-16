def solution(nums):
  """
  Method: One Pass

  [0,1,0,2,4] => [1,2,4,0,0]
  we want move the 0's to the end of the list without modifying the list
  - use zero_index pointer to keep track of the 0 element
  - iterate thought each element if it is not 0, place that element in the zero index
  and increment the zero_index, leaving the element at previous zero_index and previous spot
  it is okay, since next non-zero element will be there, or if we will replace by zero next loop
  - after 1 whole iteration of the list, # of non-zero = zero_index
  - replace zero element in from zero_index to len(nums)

  """

  zero_index = 0

  for i in range(len(nums)):
    if nums[i]:
      nums[zero_index] = nums[i]
      zero_index += 1

  for i in range(zero_index, len(nums)):
    nums[i] = 0

  

