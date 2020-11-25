

def iterativeExpandCenter(s):
  lens = len(s)
  ans = ''
  for i in range(lens):
    # get a single center palindrome
    singleCenter = expandCenter(s, i, i)
    # update the result
    if len(singleCenter) > len(ans):
      ans = singleCenter
    # get the double center palindrome
    doubleCenter = expandCenter(s, i, i+1)
    if len(doubleCenter) > len(ans):
      ans = doubleCenter

  return ans

def expandCenter(s, left, right):

  while left >= 0 and right < len(s) and s[left] == s[right]:
    # we expand from the center
    # - decrement the left
    # - increment the right
    left, right = left - 1 , right + 1
  # return the palindrome substring
  # why left + 1 ? 
  # - the loop breaks when the both end not a match
  # - left + 1 to get the previous matched palindrom
  # - right unchaged since str is sliced up to before right index
  return s[left+ 1: right]


while True:
  try:
    line = input()
    words = set()
    lens = len(line)
    for i in range(lens):
      # get a single center palindrome
      singleCenter = expandCenter(line, i, i)
      # update the result
      if len(singleCenter) > 1 and len(singleCenter) != lens:
        words.add(singleCenter)

      # get the double center palindrome
      doubleCenter = expandCenter(line, i, i+1)
      if len(doubleCenter) > 1 and len(doubleCenter) != lens:
        words.add(doubleCenter)
    d = sorted(list(words))
    for w in d:
      print(w)
    print("\n", end="")
    words = set()
  except:
    break
