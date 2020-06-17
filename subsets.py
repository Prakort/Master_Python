def solution(nums):
  """
  we want to make a copy the output [[]]
  each iteration of the number, each number will be added in the copy the array instance of the copy
  
  nums[1,2,3]
  output = [[]]
  clone = [[]]
  first iteration 1
  - add one to the clone element [1]
  - add [1] to the output [[],[1]]
  second iteration 2
  output = [[],[1]]
  clone = [[],[1]]
  add 2 into clone element, [[2],[1,2]]
  add these into the output [[],[1],[2],[1,2]]

  runtime: O(N x 2^n), generate all subset for N element, 1 element 2^n
  space: O(N x 2^), extra space to store all the subsets
  """

  output = [[]]

  for i in nums:
    # deep copy the output
    copies = copy.deepcopy(output)
    for copy in copies:
      copy.append(i)
      output.append(copy)
  return output
