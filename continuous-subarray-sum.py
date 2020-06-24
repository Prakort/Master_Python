def solution(nums, k):
  """
  Idea: it's easy to find sum from 0 to i index, what about the sum(2,5)?
  sum(0,5) - sum(0,1) = sum(2,5)
  if sum(2,5) % k == [sum(0,5) - sum(0,1)] % k then sum(0,5) % k == sum(0,1) % k
  they are the same, we should store sum % k as key, index as value

  if key exists, current index - value >= 2, we found our sub array
  """
  hm = {0:-1}
  total = 0 
  
  for i in range(len(nums)):
    total = total + nums[i]
    # prevent k = 0
    if k != 0:
      # a,b,c [1,3,4] 1%3 = 1, (1+3)%3 = 1, (1+3+4)%3 = 1, ((1+3)%3 + 4%3) = 1
      # (a+b)%k = r
      # (a+b+c)%k = d
      # (r+c)%k = d
      # 
      total %= k 

    if total in hm: 
      if i - hm[total] >= 2:
        return True
    else:
      hm[total] = i
