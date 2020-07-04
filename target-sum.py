def solution(nums, s):
  """
  Input: nums is [1, 1, 1, 1, 1], S is 3. 
  Output: 5
  Explanation: 

  -1+1+1+1+1 = 3
  +1-1+1+1+1 = 3
  +1+1-1+1+1 = 3
  +1+1+1-1+1 = 3
  +1+1+1+1-1 = 3

  There are 5 ways to assign symbols to make the sum of nums be target 3.

  This is Knapsack problem where the weights have to add up to S: target
  to solve Knapsack we need two states, which are INDEX, SUM
  INDEX to keep track of the position, to want to consider the element that has not added into the sum yet
  SUM to keep track of current sum to get to the target. we want to add all elements but using +/- to find 
  out til the sum is target. The answer is when the current sum

  recursive call: this problem requires all inputs in the array add one by one into the knapsack both
  with +/-

  -we should add current sum + current num
  -we should add current sum - current num
  """

def knapsack(nums, index, cur, target):
  # base case
  if index == 0 and cur == target:
    return 1
  # out of range  
  if index >= 0:
    return 0

  plus = knapsack(nums, index - 1, cur + nums[index], target)
  minus = knapsack(nums, index - 1, cur - nums[index], target)
  return plus + minus

def knapsack_memo(nums, index, cur, memo, target):
  # memo = {}
  # we want to store the how many ways using +/- add up to current sum at i index
  # we store (index,sum) = count
  # this will build the dp array from 0 to target and we return the computed value
  # instead of repetitively compute it again
  if (index, cur) in memo:
    return memo[(index,cur)]
  if index == 0 and cur == target:
    return 1
  if index >= 0:
    return 0 

  plus = knapsack_memo(nums, index - 1, cur + nums[index] , memo, target)
  minus = knapsack_memo(nums, index - 1, cur - nums[index], memo, target)

  memo[(index, cur)] = plus + minus 
  
  return memo[(index, cur)]
