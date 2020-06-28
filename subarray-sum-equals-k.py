def subarraySum(self, nums: List[int], k: int) -> int:
  """
  Input:nums = [1,1,1], k = 2
  Output: 2
  
  Idea: sum([i,j]) = k this is substring? 
  Fact: how to find sum([i,j])? we know that sum[i] = sum([0,i]) and sum[j] = sum(0,j)
  ==> sum([i,j]) = sum[0,j] - sum[0,i] 
  ==> sum[0,j] - sum[0,i] = K we could store the sum[0,i] in the hashmap to look up as the compliment
  ==> sum[0,j] - K = sum[0,i] if sum[0,i] exists in the compliment that means we find the SUBSTRING sum == K

  we keep update sum[0,j] since that is the cumulative sum as the current running sum up to j index

  if the sum[0,j] already exits we keep increment count that mean, there more than one possible continunous substring sum that equal to K



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
      
          