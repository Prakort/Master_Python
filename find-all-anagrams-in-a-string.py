def solution(s,p):
  lens, lenp = len(s), len(p)

  if lens < lenp:
    return []

  # store character count in the array
  # since there are only 26 char 
  # the space is constant O(1)

  sCount, pCount, res = [0]*26, [0]*26, []

  # count the p string char and increment the count
  # ord('b') - ord('a') = 1, give the right index to fix 26 array size
  for ch in p:
    pCount[ ord(ch) - ord('a')] += 1
  
  for i in range(lens):
    # count the char into sCount
    sCount[ord(s[i]) - ord('a')] += 1
    
    # when the sliding window is bigger than the len of p
    # remove/decrement count of the left window char which is i - lenp
    if i >= lenp:
      sCount[ord(s[i - lenp]) - ord('a')] -= 1

    # check if the 2 count array is the same
    if sCount == pCount:
      res.append(i - lenp + 1)

  return res
