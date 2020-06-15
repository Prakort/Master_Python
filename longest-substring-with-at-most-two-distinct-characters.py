def solution(s):
  """
  runtime: O(N) , every char in length N string is iterated over
  space: O(1), we use only 3 spaces in the hashmap
  """
  lens = len(s)

  hashmap = {}
  left = right = res = 0

  while right < lens:
    if len(hashmap) < 3:
      # store the index of the char
      hashmap[s[right]] = right 
      # move the right pointer by 1
      right += 1

    if len(hashmap) == 3:
      # find the smallest occurrence char in the hashmap
      index = min(hashmap.values())
      # delete the key/value pair
      del hashmap[s[index]]
      # move the left pointer after the deleted char index
      left = index + 1

    # update the max len
    # since right + 1 already, no need to add 1 to get the correct len
    res = max(res, right - left)

  return res
