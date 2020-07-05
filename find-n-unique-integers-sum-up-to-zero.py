def solution(n):
  """
  n = 1 : [0]
  n = 2 : [-1,1]
  n = 3 : [-1,0,1]

  if n is odd, length of ans is odd, we add zero
  if n is even, it's symetric
  max int is n//2
  """
  res = []
  for i in range(1, n//2 + 1):
    res.append(-i)
    res.append(i)

  if n % 2 == 1:
    res.append(0)

  return res
