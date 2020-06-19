def subarraySum(self, nums: List[int], k: int) -> int:
  """
  Input:nums = [1,1,1], k = 2
  Output: 2
  
  map: [
  (0:1),
  (1:1), 
  (2:1)
  ]
  sum = 1 
  sum - k = 1 - 2 = -1 not in the map
  put (1,1) in the map
  
  sum = 2 => 2 - 2 = 0 , ok 0 in the map, found the compliment
  put (2,1) in the map
  
  sum = 3 => 3 - 2 = 1 , ok 1 in the map, but why this is an answer?
        3 - 2 = 1 , (1,1) is in the map ==> means without the previous cumulative sum, we found a new sum equal to k
  """
  res = 0
  counter = Counter()
  counter[0] = 1
  s = 0
  for n in nums:
    s += n
    if (s - k) in counter:
      res += counter[s-k]
    counter[s] +=1
    
  return res
      
          