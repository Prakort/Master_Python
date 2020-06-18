def solution(nums, target):
  """
  Given a collection of candidate numbers (candidates) and a target number (target), 
  find all unique combinations in candidates where the candidate numbers sums to target.
  Each number in candidates may only be used once in the combination.

  Input: candidates = [10,1,2,7,6,1,5], target = 8,
  A solution set is:
  [
    [1, 7],
    [1, 2, 5],
    [2, 6],
    [1, 1, 6]
  ]
  
  each element could be used only once, they could be the same number but different index
  perform dfs for i in passing_index, len(nums)
  ==> (nums[i] -> current list) , (i + 1) add next element of the next index to prevent add the same index

  """

  output = []
  nums.sort()
  helper(nums, target, [], 0)

  return output
  

def helper(nums, target, path, output, index):
  if sum(path) == target:
    output.append(path)
    return 

  if sum(path) > target:
    return 

  for i in range(index, len(nums)):
    if i > index and nums[i-1] == nums[i]:
      continue 

    helper(nums, target, path + [nums[i]], i + 1)
[
  [1, 1, 1, 1, 1, 1, 1], 
  [1, 2, 3, 4, 5, 6, 7], 
  [1, 0, 3, 7, 12, 18, 25]
]
