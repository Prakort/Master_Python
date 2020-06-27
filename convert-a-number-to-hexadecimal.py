def solution(num):
  
  # base 16 
  # remainder = nums % 16
  # nums = (nums - remainder) / 16
  # if nums < 0
  # follow algo -> find the binary value of -nums ==> find the complement of binary value and add + 1 is the second complement
  # second complement in binary then convert it to hex
  # 2 ** 32 + nums = (new value) which fits the second complement of nums
  

  if num == 0:
    return '0'

  if num < 0:
    num += 2 ** 8
  l = 'abcdef'
  res = []
  while num > 0:
    r = num % 16
    num -= r
    num //= 16
    res.append(str(r) if r <= 9 else l[r-10])

  return ''.join(res[::-1])
