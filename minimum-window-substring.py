class Solution:
    def minWindow(self, s: str, t: str) -> str:
      """
      Method: sliding window
      
      we want to use 2 pointers that starts from zero index, start and end pointer
      end advances one index to the right until all chars in string t are found
      using missing as the counter of the string  t length ==> when all chars are found, missing should be zero
      
      once the all the chars in string t are found, we move the start index by one to the right to get the small window size.
      
      what happend ? we moved the start pointer and one of the char in string t is not there, then we should move the right pointer again to the right. before this, always update the res 
      
      
      
      
      """

      lens, lent = len(s), len(t)
      # window pointer
      start = end = 0
      # result
      ans = ""
      # require len
      required_len = lent
      # hashmap of the char
      window_counter = Counter(t)

      # iterate from the left to the end of the string s
      while start <= end and end < lens:
        current = s[end]
        # increment the pointer
        end += 1
        # check if the current char is in the hashmap
        # if value > 0, it is a required char that we want to have 
        # in the window
        # if value <= 0, which the char is not in the string t
        # the char is not what we want in the window
        if current in window_counter and window_counter[current] > 0:
          # decrement the required len
          required_len -= 1

        # the char has been visited, decrement the value in the hashmap
        window_counter[current] -= 1

        # SHRINKING operation
        # if the require_len == 0, which means we found all the chars in the string t in the substring of s, now we want to minimize the window
        while not required_len:
          # check the result and update since the required_len == 0
          # means, we found the window that has all the required chars

          # update the min, or ans has not been found yet
          if len(s[start: end]) < len(ans) or not ans:
            # we dont need to worry about the index
            # since we increment end + 1 above already
            # this will assign the right substring
            ans = s[start: end]


          # get the left most char
          # since we want shrik the substring in this loop
          # but still keep all the required chars that are in string t
          left_most = s[start]
          
          # increment the counter
          # since we are moving to the start index to the right 
          # why increment not decrement ?
          # when we check a char, we decrement its values in hashmap, it helps
          # differentiate the required chars values vs other chars
          # when we remove it from the window, we increment value back
          window_counter[left_most] +=1

          # this case : when we remove the required char
          # that means we have to increment the missing required_len back
          # take one out, update the lenght of required_len
          if left_most in window_counter and window_counter[left_most] > 0:
            required_len +=1

          start += 1

      return ans
