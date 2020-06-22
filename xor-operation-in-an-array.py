def solution(n, start):
  output = 0
  for i in range(n):
    output ^= start + 2*i
  return output
