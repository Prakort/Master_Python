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
