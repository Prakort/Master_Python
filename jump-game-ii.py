def jump(nums):
  
  if len(nums) < 2:
    return 0
  prev = cur = nums[0]

  res = 1
  for i in range(1,len(nums)):
    # check that it is stil in the previous jump
    # if prev < i that means, it exhausts all the steps
    # update the prev jump to the next one
    if prev < i:
      res += 1
      prev = cur
    # keep finding the total steps to get to i
    cur = max(cur, nums[i] + i)
  return (res)
