def solution(people):
  """
  [H,K]
  H: height of the person
  K: # of people with greater or equal height.

  Rearrange the queue such that H has exactly K with greater or equal infront
  - Notice H has to have K people with greater or equal height. This mean any person with shorter heigh could be in front

  [7,0],[5,0] ==> [5,0][7,0]
  this is correct since 7 has 0 # people have greater hight and same as 5
  [7,0] [5,0] [7,1] ==> [5,0] [7,0] [7,1]

  we want to take care of the tallest person first, since anyone is shorter come in between, it does not affect the K requirement. If the shortest come first and we add the taller person in, it affects the shorter person

  Method: 
  -We will short the lists as descending order for the height and ascending order for the K
  -Then we add that person based on it K index
  -If the tallest has lower K, it will be in the front and the next tallest will follow beind then if the shortest has same lower K or equal. It will goes in front the tallest. This does not affect the K requirement. That's why we have to sort based Height and K
  """
  res = []
  people.sort(key= lambda x: (-x[0], x[1]))
  
  for h in people:
    res.insert(h[1], h)
  print(res)
  
  return res
