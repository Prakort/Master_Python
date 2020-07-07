def brute_force(nums, target):
  n = len(nums)
  for i in range(n):
    for j in range(i+1, n):
      if nums[i] + nums[j] == target:
        return [i, j]
  return [0,0]

def one_pass(nums, target):
  comp = {}
  for i in range(len(nums)):
    c = target - nums[i]
    if c in comp:
      return [comp[c], i]
    comp[nums[i]] = i

  return [0,0]
