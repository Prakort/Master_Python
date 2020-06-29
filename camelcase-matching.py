def solution(quries, pattern):
  """
  we want to check each word one by one if the pattern matches
  -use start pointer track the pattern char
  -iterator normally over the word 
  -if char matches the pattern, increment start pointer and continue to the next iteration that means the char is UPPERCASE and MATCHED
  -if any char is UPPERCASE and does not match, result is False
  
  -out of the loop, we should finish iterator over the pattern as well as the word then start should not be less than len(pattern)
  """

  res = []

  for word in quries:
    flag = True 
    # start from the beginning of the pattern
    # reset every iteration
    start = 0

    for i in range(len(pattern)):
      # if char matches the pattern
      if start < len(pattern) and word[i] == pattern[start]:
        # move to the next pattern char
        start += 1
        continue
      # it fails above condition, then it does not matches the pattern
      # just flag to false
      if word[i].isupper():
        flag = False 

    # make sure that all patterns have been matched
    if start < len(pattern):
      flag = False 

    res.append(flag)

  return res
