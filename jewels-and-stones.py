def solution(J, S):
  counter = 0 
  
  for i in S:
    if i in J:
      counter += 1
      
  return counter
