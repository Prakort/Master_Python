def solution(nums):
  """
  find a signle number in the list
  XOR: 
  1 xor 0 = 1
  0 xor 1 = 1
  1 xor 1 = 0
  0 xor 0 = 0

  a xor 0 = a
  1 xor 0 xor 1 = 0
  1 xor 2 xor 2 = 1
  we will xor to find the a signle occurrence
  """
  n = 0
  for i in nums:
    n ^= 0

  return n
