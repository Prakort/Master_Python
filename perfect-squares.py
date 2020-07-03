def solution(target):
  """
  We want to find the number of square number that sum up to target

  - first we have to find the upperbound of the square number
  let's target = 10, upperbound n =3 which n^2 = 9, we dont need to do
  extra caculcation that wont help the sum because they are greater than the sum
  - we use sqrt(target) and cover to int and generate the square number from 1 to that upperbound
  - now that we have list of square since, those numbers <= target
  that mean we could find the sum by doing substract, target - square = m 
  target - square count as 1 since we use 1 square, all we need to know that how many
  square number that add up to m, from this could just build an array from 1 to target
  with each cell represent the number of square number that sum to the index and we store only 
  the minimum count

  - now we build a dp array bottomup, such that we reach the target, we have all the precompted value of the compliment
  like m above

  runtime: O(n*sqrt(n)) : we iterate from 0 to target and inner loop with sqrt(target) is length
  space: O(n), we need target + 1 space to store the counts
  """
  #let find the upperbound
  upper = int(str(target))
  #let build the square number list, need to have upper square
  squares = [ i**2 for i in range(1, upper+1)]
  #let define a dp array from 1 to target
  dp = [float(int)] * (target+1)
  # base case 
  dp[0], dp[1] = 0, 1

  for i in range(1, target+1):
    for square in squares:
      if square > i:
        break
      dp[i] = min(dp[i], dp[i - square] + 1)

  return dp[-1]
