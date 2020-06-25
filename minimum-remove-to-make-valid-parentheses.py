def solution(s):
  """
  our goal to remove all extra ( or )
  Method: Two pass
  first pass, remove ')'
  second pass, remove '('

  """
  stack, res = [], []

  for i in range(len(s)):
    # always add every char in the res
    res.append(s[i])
    # check if it is '('
    if s[i] == '(':
      # add index into the stack
      stack.append(i)
    elif s[i] == ')':
      # always check if the stack is not empty mean there is '(' to match
      if stack:
        stack.pop() # match then pop()
      else:
        # there is no '(' in the stack
        # ')' is extra
        res[i] = '' # remove it from the result

  # second pass
  # if stack is not empty, mean there are not enough ')' to match
  # remove '(' 
  for i in stack:
    res[i] = ''

  return ''.join(res)
