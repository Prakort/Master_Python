def solution(prices):
  """
  Goal: is to make as many transactions as possible to make max profit
  Method: we have to buy low and sell high, then we check every pair prices and make transaction
  """
  maxProfit = 0
  for i in range(1, len(prices)):
    if prices[i] > prices[i-1]:
      maxProfit += prices[i] - prices[i-1]

  return maxProfit

def valley_peek(prices):
  """
  Same idea as mention, we want to make max profit with many transactions
  then we first must find the LOCAL minimum and its next LOCAL maximum and make transaction,
  and keep repeating the process until no more stock
  """
  n = len(prices)
  maxProfit = i = 0 
  localMin = localMax = prices[0]
  
  while i < n - 1:
    # keep iterating to find the LOCAL min
    while i < n and prices[i] >= prices[i+1]:
      i +=1
    # while loop break that means we find the local min
    localMin = prices[i]

    # keep iterating to find the LOCAL max
    while i < n and prices[i] <= prices[i-1]:
      i +=1
    # we find the local max
    localMax = prices[i]

    maxProfit += localMax - localMin
  
  return maxProfit


