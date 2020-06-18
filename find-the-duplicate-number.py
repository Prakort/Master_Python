def solution(nums):
  """
  [1,2,3,4,2]
  Given array containing n+1 integer between 1 and n inclusive 
  - we know that array stores only pos+v in, we use negation to mark
  - if we just the element as the index, it never gets out of range since there are n + 1 integer
  - use the element as the index and muliply that nums[index] * -1 to make as visited ==> every signle element 
  will cause the nums[index] become negative
  - what about the 0 zero index, since int start from 1 and n, we ignore the nums[zero] index element because zero in not in the range
  - every element should be positive at first and become negative
  - first an element is check twice for negative that means the element has been visited already ==> there exists duplicate
  of the index the return the element 

  e.g [1,3,4,2,2]
  - [1,-3,4,2,2] index = abs(nums[0]) = 1 ===> nums[1] = -1
  - [1,-3,4,-2,2] index = abs(nums[1]) = 3 ===> nums[3] = -2
  - [1,-3,4,-2,-2] index = abs(nums[2]) = 4 ===> nums[4] = -2
  - [1,-3,-4,-2,-2] index = abs(nums[3]) = 2 ===> nums[2] = -4
  - [1,-3,-4,-2,-2] index = abs(nums[4]) = 2 ===> nums[2] < 0 ===> return 2 

  runtime: O(n), every element in the array length N is visted
  space: O(1)

  """

  for n in nums:
    # convert element to index
    index = abs(n)
    # check if the element has been visited, negative element has been marked as visited
    if nums[index] < 0:
      return index 
    # mark element by negative magnitude
    nums[index] *= -1

def solution2(nums):

  """
  Method: One pass

  using set()  to check if the element has been added twice

  """
  check = set()

  for n in nums:
    if n in check:
      return n

    check.add(n)
