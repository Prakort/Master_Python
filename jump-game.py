def canJump(nums):
  n = len(nums)
  m = i = 0
  # m is the number of step of each element
  # if one of step is greater than the length
  # we could reach the end
  # m = max(m, newSteps)
  # newSteps < m which is current step
  # check newSteps + 1
  # until we find the newSteps that will reach the end
  # other, run out of step in m
  # could find element to jump to the end
  # that means we could not reach the end 
  while i <= m:
    m = max(m, nums[i] + i)
    if m >= n - 1:
      return True
    i += 1
  return False

def reverse(nums):
  
  n = len(nums)
  end = n - 1
  # we want to move end to index 0
  # that means it is reachable from the start to end
  for i in reversed(range(n)):
    # i = number of steps to get to i 
    # nums[i] = number of steps, it could jump
    # i + nums[i] = total of steps, from 0 to up i index
    # if i + nums[i]
    total_steps_up_to_i = i + nums[i]
    if total_steps_up_to_i >= end:
      # end is reachable by end - 1
      # move end inside
      # find out if next index could reach end
      end = i
    
  # if end is 0, that means, the last index is reachable
  return not end
    
def solution3(nums):
  n = len(nums)

  steps = nums[0]

  for i in range(1, n):
    if steps < i :
      return False
    steps = max(steps, nums[i] + i)

  return True
