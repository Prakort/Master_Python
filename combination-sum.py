def solution(nums, target):
  output = []
  dfs(nums, [], target, output, 0)

def dfs(nums, path, target, output, index):
  if sum(path) == target:
    output.append(path)
    return 

  if sum(path) > target:
    return 

  for i in range(index, len(nums)):
    dfs(nums, path + [nums[i]], target, output, index )
  
