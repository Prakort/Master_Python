def solution(k, n):
  """
  [1..9] find the array of k length that the total is n

  define the 1-9 array
  we want to do dfs to get all possible value but duplicate value
  since the [1..9] is already sorted, we dont have to worry

  - base case: length(current list) == k and sum(current list) == n : add into the result
  - base case: length(current list) >= k or sum(current list) >= n: return : mean that it failed the conditions
  1, length is greater than k or the sum is greater than n

  iterate from the passing_index to the end of list to find next element:
  - add the current element into the current list, passing the new index + 1 for the next element prevent duplicate

  """
  output = []
  helper(k, n, output, [], 0)
  return output 
  
def helper(k, n, output, path, index):
  # meet the conditions
  if len(path) == k and sum(path) == n:
    output.append(path)
    return 
  # fails the conditions, reject the them
  if len(path) >= k or sum(path) >= n:
    return 

  for i in range(index, 9):
    helper(k, n, output, path + [i+1], i)
