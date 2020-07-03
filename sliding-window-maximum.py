def brute_force(nums, k):
  """
  we will start from up to len(nums) - k + 1
  that the lowerup will the subset will travel up to
  Input: nums = [1,3,-1,-3,5,3,6,7], and k = 3
  Output: [3,3,5,5,6,7] 
  Explanation: 

  Window position                Max
  ---------------               -----
  [1  3  -1] -3  5  3  6  7       3
  1 [3  -1  -3] 5  3  6  7       3
  1  3 [-1  -3  5] 3  6  7       5
  1  3  -1 [-3  5  3] 6  7       5
  1  3  -1  -3 [5  3  6] 7       6
  1  3  -1  -3  5 [3  6  7]      7

  left pointer travel up to len(nums) - k + 1 which at index 5 cell: 3, upper range is len(n)
  it is just i + k is the upper bound of the subarray

  we could find max for which subarray [i:i+k], append in the result list
  how many subarray which k element of length n
  it's n - k 
  we iterate through k element to find the max?
  runtime = (n-k)*k = nk which n > k
  space: n-k space if count the result list l, if we dont , O(1)
  """
  res = []
  lower = len(nums) - k + 1
  for i in range(lower):
    upper = i + k
    res.append(max(nums[i:upper]))
  return res 

def optimized(nums, k):
  """
  same idea above but we want to make it faster, without finding a max number in k element
  which is repetitive

  1-case
  we want to store the index of the element because we could just it to check if the index
  is out of the scope of k then we want to remove it, whether it is a max from previous k element

  2-case
  we always append the index to the right and we want to keep the max of k element in the front of the deque
  if we move the k subarray by 1, we want to check that remove all the elements that are less that this current element
  if all of the indexs represent the numbers less that current element, then we remove all of them, until current element less 
  than the last element in deque. this allows us to keep track of the largest number from previous k and the new k subarray

  why we pop from right to left until current < last element in the deque
  -answer: because if current element is the new max, deque will be empty, we add the new max
  else there exists the max from previous k, but we still want to keep the current element because in case
  it will be a max for the next k sub array and the element in deque that greater than current element
  will be remove by the first case since it's out of range for k subarray
  """
  res = []
  deck = deque()

  for i in range(len(nums)):
    # case-1: remove all the indexes that are out of k subarray
    while deck and deck[0] < i - k + 1:
      deck.popleft()

    # case-2: remove indexes from right to left if they are less than current elememt
    while deck and nums[deck[-1]] < nums[i]:
      deck.pop()

    # append index to the right
    deck.append(i)

    # get the max which is the front element of deque
    if i >= k - 1:
      res.append(nums[deck[0]])
  
  return res 
