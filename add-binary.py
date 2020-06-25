def solution(a, b):

  i = len(a) - 1
  j = len(b) - 1 
  carry = 0
  res = [] 
  
  while i >= 0 or j >= 0:
    x = 1 if i>= 0 and a[j] == '1' else 0
    y = 1 if j>= 0 and b[j] == '1' else 0 

    _sum = x + y + carry 
    carry = _sum // 2
    res.append('1' if _sum > 1 else '0')

    i -= 1
    j -= 1

  if carry != 0:
    res.append('1')

  return ''.join(reversed(res))
