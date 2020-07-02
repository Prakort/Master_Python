
def solution(nums):
  """
  we want to get all combinations of the element in the list
  then we have iterate on each element and perform a dfs for each element to get all the different possible combination
  - we want to start reading the start of the list every time
  - we will just slice the origial list without the current element and add current element into the path
  - once the slicing nums is empty, then we added all combinations in the path list
  """
  res = []
  dfs(nums,[])
  return res

def dfs(nums, path, res):
  # base case
  if 0 == len(nums):
    res.append(path)
    return

  for i in range(len(nums)):
   dfs(nums[:i]+ nums[i+1:], path + [nums[i]], res)

        
        
        