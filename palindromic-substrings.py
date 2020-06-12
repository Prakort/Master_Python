def iterative(s):
  """
  expand from the center of each index 
  left = index - 1 
  right = inde + 1
  always check the lower and upper bound of the two
  
  we have to check 2 types of palindrome 
  1- baab double center 
  2- bab single center
  
  to find double center, in the first loop we check str[index] == str[right] and keep increment right 
  
  e.g baab, baaab when right at b. the first loop ends since index a != index right b anymore 
  
  this when the second loop start to pick up where the first loop left off. right index has been incremented and second loop check str[left] == str[right]. in e.g they match and we keep increment the counter
  
  if we didnt find the double char in the first loop
  then second will start find the a single center right away to expand 
  
  """
  lens = len(s)
  if lens == 0:
    return 0
  count = 0
  
  for i in range(lens):
    left, right = i-1, i+1
    count +=1
    while right < lens and s[i] == s[right]:
      count += 1
      right += 1
      
    while left >=0 and right < lens and s[right] == s[left]:
      count += 1 
      left -= 1
      right += 1
      
  return count
      