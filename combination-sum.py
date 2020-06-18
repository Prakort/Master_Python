def solution(nums, target):

  """
  Method: DFS
  with [] start with every element in the list and find the sum equals to the target

  - base condition is sum([]) == target then add the list into the result
  - optimize if sum([]) > target exits right away
  - loop through from passing_index_to_start to the length
  - and add the current num into the list for the iteration

  runtime: O((n + k)!) each element is iterated n(n-1)(n-2).....1 = n! and k is the maximum that a signle element repeated
  space: O(m) m is the size of the ouput solution
  
  """
  output = []
  dfs(nums, [], target, output, 0)

def dfs(nums, path, target, output, index):
  if sum(path) == target:
    output.append(path)
    return 

  if sum(path) > target:
    return 

  for i in range(index, len(nums)):
    dfs(nums, path + [nums[i]], target, output, i)
  
