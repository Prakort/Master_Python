def solution(nums):
  
  n = len(nums)
  max_sum = cur_sum = 0

  for i in range(1, n):
    # update the current sum with new sum
    cur_sum = max(cur_sum, nums[i] + cur_sum)
    # update the max with new found sum
    max_sum = max(max_sum, cur_sum)

  return max_sum
