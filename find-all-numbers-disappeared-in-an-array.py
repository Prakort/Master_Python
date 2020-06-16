def solution(nums):
  """
  Method: One Pass x twice

  we want to find the missing number inclusive 1 - N where N = len(nums)
  - first we need an extra array with length + 1 since the element in nums start with 1
  - new array index is the element from nums, value is 1
  - goes through the new, which index has zero value is the missing number

  runtime: O(N), every element in the array with length N is visited
  space: O(N+1), since we use an extra array to hold all the indexes from the nums
  """

  n = len(nums)
  temp = [0] * (n+1) # add an extra space
  result = []

  for i in nums:
    temp[i] = 1

  for i in range(1, n+1):
    if not temp[i]:
      result.append(i)

  return result


def solution2(nums):
  """
  Method: One Pass x twice

  instead of using an extra array, we want tranform the element into a new index
  face: we know that element 1 - N, all element are not out of range
  let new_index = element - 1 and mark that nums[new_index] with -1 * nums[new_index]
  this means in the second loop, if the element in the index that is positive, it is the missing number

  """
  result = []

  for i in range(len(nums)):
    index = abs(nums[i]) - 1

    if nums[index] > 0:
      nums[index] *= -1

  for i in range(len(nums)):
    if nums[i] > 0:
      # i + 1 is the right number, since we - 1 from the top
      result.append(i + 1)
