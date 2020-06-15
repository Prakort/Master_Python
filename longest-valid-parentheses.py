def longestValidParentheses(self, s: str) -> int:
  """
  Method: Stack 

  We store the index of the open '(' only
  once we found the close ')', pop the top '('
  find the lenght index - top index which could be -1, to get the offset
  or if the stack is empty because of the first close ')' add the current index to restore the index
  """
  len_s = len(s)
  stack, max_len = [], 0
  stack.append(-1)
  for i in range(len_s):
    if s[i] == '(':
      stack.append(i)
    else:
      stack.pop()
      if not stack:
        stack.append(i)
      else:
        max_len = max(max_len, i - stack[-1])
        print('i',i,'top',stack[-1])
  return max_len
