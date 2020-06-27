def solution(num):


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
