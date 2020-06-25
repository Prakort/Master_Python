def solution(num1, num2):
  def _int(_s):
    return ord(_s) - ord('0')
  def _str(_n):
    return chr(_n + ord('0'))
    
  i = len(num1) - 1
  j = len(num2) - 1
  carry = 0 
  res = []
  while i >= 0 or j >= 0:
    x = _int(num1[i]) if i>=0 else 0
    y = _int(num2[j]) if j>=0 else 0
    
    _sum = x + y + carry 
    carry = _sum // 10
    res.append(_str(_sum%10))
    
    i -=1
    j -=1
    
  if carry != 0:
    res.append('1')
    
  return ''.join(reversed(res))
    
  