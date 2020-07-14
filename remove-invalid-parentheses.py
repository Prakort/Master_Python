def remove_parenthese(s):
  """
  we want to keep track of the number of open and close that we have to remove
  still keep the valid paren to do so, we have to remove the extra open or close when need to
  and keep increment index. Add anything to the path if they are extra open or close
  to make a valid make, we use the need_close to keep track of number of open paren are needed to be closed
  
  runtime O(2^N)
  space: O(N)
  """

  #find the extra close or open
  #both of them has to be zero
  extra_open = extra_close = 0
  for ch in s:
    if ch == '(':
      extra_open += 1
    elif ch == ')':
      # if it's valid, extra_open is greater than 0
      if extra_open > 0:
        extra_open -= 1
      # there is an extra close paren
      else:
        extra_close += 1

  res = set()
  # helper()
  return res

def helper(s, index, need_close, extra_open, extra_close, path, res):
  #base case
  if index == len(index):
    if extra_open == 0 and extra_close == 0:
      res.add(path)
    return 
  else:
    if s[index] == '(' and extra_open > 0:
      helper(s, index + 1, need_close, extra_open - 1, extra_close, path, res)
    elif s[index] == ')' and extra_close > 0:
      helper(s, index + 1, need_close, extra_open, extra_close, path, res)
    
    ch = s[index]
    path += ch
    if ch != '(' and ch != ')':
      helper(s, index + 1, need_close, extra_open, extra_close, path, res)
    elif ch == '(':
      helper(s, index + 1, need_close + 1, extra_open, extra_close, path, res)
    elif ch == ')':
      if need_close > 0:
        helper(s, index + 1, need_close - 1, extra_open, extra_close, path, res)

      


