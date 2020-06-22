def solution(nums):
  counter = 0

  while nums > 0:
    nums = (nums // 2) if nums % 2 == 0 else (nums - 1)
    counter += 1

  return counter 
