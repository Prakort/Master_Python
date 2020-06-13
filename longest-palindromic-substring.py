def dp(s):
  lens = len(s)

  # store boolean in each cell
  dummy = [[False for i in lens] for i in lens]

  ans, count = '', 0
  for end in range(lens):
    for start in range( end + 1):
      # check the both end char if they match
      isMatched = s[end] == s[start]

      # 1 and 2 length of char, substring
      # update the cell to be True
      if end - start < 2 and isMatched:
        dummy[start][end] = True 

      # substring with length 3 and more
      # - check the both end of the substring: isMatched
      # - check the the inner substring with start + 1, end -1 
      # since we already computed, if the inner substring is a panlidrome and both end char match
      # it is a palindrome

      if end - start >= 2 and isMatched and dummy[start + 1][end  - 1]:
        dummy[start][end] = True 

      # update the max len and answer
      # end index - start index + 1 gives the correct length of the substring
      # if it is larger than the previous count and the both indexes in the dummy is True
      # update the result
      if end - start + 1 > count and dummy[start][end]:
        count = end - start + 1
        ans = s[start: end + 1]

  return ans
        
      
"""
We want to iterate on every char of the string and apply the expand from center method on the index of that char

- aba is a single center palidrome ==> check expandCenter(s, i, i)
- abba is a double center palidrome ==> check expandCenter(s, i, i + 1)

keep checking the expand and check the outter char on both end 
until they are not the same and return the previous palindrome substring 

once we get the palidromic substring, we update the result

runtime: O(N^2), there are N elements and every single char in the str is being iterated over, and each index
we apply expandCenter func which could iterator up to N chars of the string.

space: O(1), we are not using any space. all the operations are O(1)

"""
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
