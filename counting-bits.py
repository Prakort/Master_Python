def solution(num):
  """
  What is the question?
  return the list of the number of 1's representing each number from 0 up to nums
  5
  0: 000
  1: 001
  2: 010
  3: 011
  4: 100
  5: 101
  result: [0,1,1,2,1,2]
  
  notice that 
  4: 100 and 4 >> 1 : 100 >> 1 : 10 is 2
  5: 101 and 5 >> 1 : 101 >> 1 : 10 is 2
  but number of 1's is +1
  
  so we notice that # of 1's of n is just # of n/2 plus 1 if n is odd
  """
  
  res = [0] * (num + 1)
  for i in range(1,len(res)):
    res[i] = res[i>>1] + (i%2)
    
  return res
