def solution(prices):
  res = []
  n = len(prices)
  for i in range(n):
    buy = prices[i]
    for j in range(i+1, n):
      if prices[j] <= buy:
        buy -= prices[j]
        breakpoint
  
  return buy



def use_stack(prices):
  """
  We use stack to store the index from the end of the list since index i always look to the right index j then using stack allows us to read and know all values from index j toindex i

  If index in the stack represent the price higher than current price, we will keep popping until stack is empty or we find the smaller price

  """
  n = len(prices)
  stack, res = [], []
  for i in reversed(range(n)):
    if not stack:
      res.append(prices[i])
    else:
      while stack and prices[stack[-1]] > prices[i]:
        stack.pop()
      if len(stack) != 0:
        res.append(prices[i] - prices[stack[-1]] )
      else:
        res.append(prices[i])
    stack.append(i)
  return reversed(res)
