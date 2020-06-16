def solution(prices):
  """
  Method: One pass

  we want to find the smallest price to buy and highest price to sell 
  must buy before selling

  - iterate through the price, find the smallest and update the min_price vs i
  - update max_profit by substract current value - min_price, since we already buy first
  then we dont have to worry about the other
  """
  max_profit, min_price = 0, float('inf')

  for price in prices:
    min_price = min(price, min_price)
    max_profit = max(price - min_price, max_profit)

  return max_profit
