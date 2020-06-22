def solution(nums):
  counter = 0 
  for n in nums:
    counter += 1 if (len(str(n)) % 2== 0 ) else 0
  return counter
