def solution(nums):
  # runtime: O(n), since we skip n - 1 if it exists in the set
  # if only the start of the longest streak is up to O(n)
  # space: O(n), store all nums in the sets
  sets = set(nums)
  res = 0 

  for n in nums:
    start = 1
    # if there exists smaller number, skip
    # will start from that smaller num instead
    if n - 1 in sets:
      continue
    if (n + 1) in sets:
      while n + 1 in sets:
        start += 1
        n += 1
        
    res = max(res, start)
  return res
  
