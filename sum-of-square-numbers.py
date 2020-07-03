def solution(c):
  """
  we want to find the 2 of square number that sum up to c
  we could store all the i**2 up to sqrt(c)
  """
  squares = set([i**2 for i in range(int(sqrt(c))+1)])

  for sq in squares:
    if c - sq in squares:
      return True 

  return False
